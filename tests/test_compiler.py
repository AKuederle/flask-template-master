import pytest
from pytest import raises

from flask_template_master.compiler import BaseCompiler, SendFileCompiler, LatexCompiler


def test_base_compiler_raises_error():
    with raises(NotImplementedError) as exc_info:
        BaseCompiler().compile('', '')
    assert exc_info.type == NotImplementedError


@pytest.fixture(scope='module')
def file_compiler():
    return SendFileCompiler()


@pytest.fixture(scope='module')
def latex_compiler():
    return LatexCompiler()


@pytest.fixture(scope='module')
def minimal_tex():
    return r"""
    \documentclass{article} 
    \begin{document}
    First document. This is a simple example, with no 
    extra parameters or packages included.
    \end{document}"""


def test_file_compiler_attachment_header(file_compiler, app):
    response = file_compiler.compile('test', 'test_text')
    assert 'attachment' in response.headers['Content-Disposition']


def test_file_compiler_sends_created_name(file_compiler, app, monkeypatch):
    monkeypatch.setattr(file_compiler, '_build_file_name', lambda x: 'mock_called')
    response = file_compiler.compile('test', 'test_text')
    assert 'filename=mock_called' in response.headers['Content-Disposition']


def test_build_filename():
    compiler = SendFileCompiler(file_extension='ext', file_prefix='pre', file_postfix='post')
    assert compiler._build_file_name('file') == 'prefilepost.ext'


def test_latex_compiler_works(latex_compiler, app, minimal_tex):
    response = latex_compiler.compile('test', minimal_tex)
    assert 'application/pdf' in response.headers['Content-Type']
    assert response.response.file.raw.read().startswith(b'%PDF')
