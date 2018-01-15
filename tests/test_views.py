import pytest
from flask import json

from flask_template_master.views import create_template_endpoint


class TestSimpleEndpoints:
    endpoint = '/test/'

    @pytest.fixture(autouse=True)
    def setup_endpoint(self, app, api, default_environment):
        create_template_endpoint(api, self.endpoint, environment=default_environment[0])
        api.init_app(app)

    def test_index(self, client):
        response = client.get(self.endpoint)
        assert response.status_code == 200, 'Index not reachable'

    def test_templates(self, client, default_environment):
        for template in default_environment[1].keys():
            response = client.get(self.endpoint + template)
            assert response.status_code == 200, 'Template endpoint not reachable'

    def test_index_returns_list_of_templates(self, client, default_environment):
        response = client.get(self.endpoint)
        json_response = json.loads(response.get_data(as_text=True))
        assert set(json_response['templates']) == set(default_environment[1].keys())

    def test_vars_returned_on_get(self, client):
        for template, var in zip(['a', 'b'], [{'a'}, {'a', 'b'}]):
            response = client.get(self.endpoint + template)
            json_response = json.loads(response.get_data(as_text=True))
            assert set(json_response['vars']) == var

    def test_template_name_returned_on_get(self, client, default_environment):
        for template in default_environment[1].keys():
            response = client.get(self.endpoint + template)
            json_response = json.loads(response.get_data(as_text=True))
            assert json_response['template_name'] == template

    def test_template_source_returned_on_get(self, client, default_environment):
        for template, source in default_environment[1].items():
            response = client.get(self.endpoint + template)
            json_response = json.loads(response.get_data(as_text=True))
            assert json_response['source'] == source
