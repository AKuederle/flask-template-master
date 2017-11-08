import pytest
from flask import Flask

from jinja2 import Environment, DictLoader
from flask_template_master import Api


class TestConfig:
    TESTING = True


@pytest.fixture
def app():
    """An application for the tests."""
    _app = Flask('test')
    _app.config.from_object(TestConfig)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.yield_fixture
def client(app):
    """A Flask test client. An instance of :class:`flask.testing.TestClient`
    by default.
    """
    with app.test_client() as client:
        yield client


@pytest.fixture
def api():
    return Api()


@pytest.fixture
def default_environment():
    templates = {'a': 'a:{{ a }}', 'b': 'b:{{ b }}, a:{{ a }}'}
    return Environment(loader=DictLoader(templates)), templates
