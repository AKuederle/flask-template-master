from flask_restful import Resource
from flask import request
import fnmatch
from jinja2 import meta


class BaseTemplateView(Resource):
    """Base View To Provide Templates.

    Attributes:
        GLOBALS: A dictionary of variables that is shared by all templates
        ENVIRONMENT: A jinja2 Environment providing a template loader that supports list_templates
    """
    ENVIRONMENT = None
    GLOBAL_PROVIDER = None

    def get(self, template_name=None):
        """Return list of templates or details of a single template"""
        if not template_name:
            match_filter = request.args.get('filter', default='*', type=str)
            return {'templates': self.ENVIRONMENT.list_templates(filter_func=lambda x: fnmatch.fnmatch(x, match_filter))}
        source = str(self.ENVIRONMENT.loader.get_source(self.ENVIRONMENT, template_name)[0])
        return_dict = {
            'template_name': template_name,
            'source': source,
            'vars': list(meta.find_undeclared_variables(self.ENVIRONMENT.parse(source)))
        }
        if self.GLOBAL_PROVIDER:
            return_dict['globals'] = self.GLOBAL_PROVIDER.get_globals()
        return return_dict

    def post(self, template_name):
        """Post data to a template and return a rendered template."""
        if request.is_json:
            vars = request.get_json().get('vars', {})
        else:
            vars = {}
        if self.GLOBAL_PROVIDER:
            vars = {**self.GLOBAL_PROVIDER.get_globals(), **vars}
        return self.ENVIRONMENT.get_template(template_name).render(**vars)

    @classmethod
    def add_as_resource(cls, api, base_route, argument=None):
        argument = argument or '<string:template_name>'
        api.add_resource(cls, base_route, base_route + argument)


def create_template_endpoint(api, base_route, argument=None, environment=None, global_provider=None):
    class_dict = {
        'ENVIRONMENT': environment,
        'GLOBAL_PROVIDER': global_provider
    }
    class_view = type(''.join(e for e in base_route if e.isalnum()), (BaseTemplateView, ), class_dict)
    class_view.add_as_resource(api, base_route, argument)
    return class_view
