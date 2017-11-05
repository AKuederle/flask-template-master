from flask_restful import Resource
from flask import request
import fnmatch
from jinja2 import meta


class _BaseTemplateListView(Resource):
    ENVIRONMENT = None

    def get(self):
        """Return list of templates"""
        match_filter = request.args.get('filter', default='*', type=str)
        return {'templates': self.ENVIRONMENT.list_templates(filter_func=lambda x: fnmatch.fnmatch(x, match_filter))}


class _BaseTemplateView(Resource):
    ENVIRONMENT = None
    GLOBALS = {}

    def get(self, template_name):
        """Return list of templates or details of a single template"""
        source = str(self.ENVIRONMENT.loader.get_source(self.ENVIRONMENT, template_name)[0])
        return {
            'template_name': template_name,
            'source': source,
            'vars': list(meta.find_undeclared_variables(self.ENVIRONMENT.parse(source)))
        }

    def post(self, template_name):
        """Post data to a template and return a rendered template."""
        vars = request.get_json()['vars']
        print(vars)
        return self.ENVIRONMENT.get_template(template_name).render(**vars)


class BaseTemplateView:
    """Base View To Provide Templates.

    Attributes:
        GLOBALS: A dictionary of variables that is shared by all templates
        ENVIRONMENT: A jinja2 Environment providing a template loader that supports list_templates
    """
    ENVIRONMENT = None
    GLOBALS = {}

    _TEMPLATE_LIST_VIEW = _BaseTemplateListView
    _TEMPLATE_VIEW = _BaseTemplateView

    @classmethod
    def add_as_resource(cls, api, base_route, argument=None):
        argument = argument or '<string:template_name>'
        # Handle taht via __new__ or metaclass
        cls._TEMPLATE_LIST_VIEW.ENVIRONMENT = cls.ENVIRONMENT
        cls._TEMPLATE_VIEW.ENVIRONMENT = cls.ENVIRONMENT
        cls._TEMPLATE_VIEW.GLOBALS = cls.GLOBALS
        api.add_resource(cls._TEMPLATE_LIST_VIEW, base_route)
        api.add_resource(cls._TEMPLATE_VIEW, base_route + argument)
