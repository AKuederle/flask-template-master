from flask import Flask


def create_app(config_object=None):
    """Application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split('.')[0])
    if config_object:
        app.config.from_object(config_object)

    from test_project.views import api
    app.register_blueprint(api)


    return app
