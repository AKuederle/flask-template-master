import pytest
from pytest import raises

from flask_template_master.compiler import BaseCompiler, SendFileCompiler


def test_base_compiler_raises_error():
    with raises(NotImplementedError) as exc_info:
        BaseCompiler().compile('', '')
    assert exc_info.type == NotImplementedError


@pytest.fixture(scope='module')
def file_compiler():
    return SendFileCompiler()


def test_file_compiler_attachment_header(file_compiler, app):
    response = file_compiler.compile('test', 'test_text')
    assert 'attachment' in response.headers['Content-Disposition']


def test_file_compiler_sends_created_name(file_compiler, app, monkeypatch):
    monkeypatch.setattr(file_compiler, '_build_file_name', lambda x: 'mock_called')
    response = file_compiler.compile('test', 'test_text')
    assert 'filename=mock_called' in response.headers['Content-Disposition']