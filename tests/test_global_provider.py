import pytest
from pytest import raises

from flask_template_master.global_provider import DictGlobalProvider, BaseGlobalProvider


@pytest.fixture(scope='module')
def dict_provider():
    return DictGlobalProvider({'a': 1, 'b': 2})


def test_dict_provider_returns_globals(dict_provider):
    assert dict_provider.get_globals() == {'a': 1, 'b': 2}


def test_base_provider_raises_error():
    with raises(NotImplementedError) as exc_info:
        BaseGlobalProvider().get_globals()
    assert exc_info.type == NotImplementedError

