import subprocess

import os
from tempfile import gettempdir

from io import BytesIO
from flask import send_file


class BaseCompiler:
    def compile(self, template_name, document):
        raise NotImplementedError()


class SendFileCompiler(BaseCompiler):
    """A simple compiler that tries to send the compiled template as a file instead of a simple request content."""
    FILE_EXTENSION = None
    FILE_PREFIX = None
    FILE_POSTFIX = None

    def __init__(self, file_extension=None, file_prefix=None, file_postfix=None):
        self.FILE_EXTENSION = file_extension or self.FILE_EXTENSION
        self.FILE_PREFIX = file_prefix or self.FILE_PREFIX
        self.FILE_POSTFIX = file_postfix or self.FILE_POSTFIX

    def _build_file_name(self, template_name):
        file_name = ''
        extension = '.' + self.FILE_EXTENSION if self.FILE_EXTENSION else None
        for part in [self.FILE_PREFIX, template_name, self.FILE_POSTFIX, extension]:
            if part:
                file_name += part
        return file_name

    def _create_file(self, template_name, document):
        buffer = BytesIO()
        buffer.write(document.encode('utf-8'))
        buffer.seek(0)
        return buffer

    def compile(self, template_name, document):
        file = self._create_file(template_name, document)
        return send_file(file, attachment_filename=self._build_file_name(template_name),
                         as_attachment=True)


class LatexCompiler(SendFileCompiler):
    LATEX_COMMAND = 'pdflatex'
    _OUT_DIR = gettempdir()
    _TEMP_OUT_NAME = 'temp'
    FILE_EXTENSION = 'pdf'

    def _create_file(self, template_name, document):
        tempfile = os.path.join(self._OUT_DIR, self._TEMP_OUT_NAME)
        temp_tex = tempfile + '.tex'
        with open(temp_tex, 'wb') as f:
            f.write(document.encode('utf-8'))
        proc = subprocess.Popen([*self.LATEX_COMMAND.split(' '), temp_tex], cwd=self._OUT_DIR)
        proc.wait()
        return tempfile + '.' + self.FILE_EXTENSION
