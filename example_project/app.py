from flask import Flask


def create_app(config_object=None):
    """Application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split('.')[0])
    if config_object:
        app.config.from_object(config_object)

    from example_project.views import api
    api.init_app(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run('0.0.0.0', 5000, debug=True)