flask-template-master
=====================

.. image:: https://img.shields.io/pypi/v/flask-template-master.svg
    :target: https://pypi.python.org/pypi/flask-template-master
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/AKuederle/flask-template-master.png
   :target: https://travis-ci.org/AKuederle/flask-template-master
   :alt: Latest Travis CI build status

This is a little Python package, that allows you to run a small templating webserver in a handfull lines of code.
This webserver can handle all your default email responses, create customized letter heads or even create dynamically generated PDFs.
The idea is, you set up the server with access to all your template files and send it a set of variables.
In return you will get you template text with all your variables included or even directly a beautifully rendered PDF file.
The webserver is based on flask and flask-restfull and uses the jinja templating language.

Features:

- Support for multiple Template Loader and multiple endpoints
- Integrate it seamlessly in bigger flask applications (this means you can handle your login and permission system)
- Support for global variables, that can be accessed by all templates
- Easy to extend by subclassing the provided models

Roadmap 1.0 Release
-------------------
- Auto pypi publishing
- Documentation

Longterm Roadmap
----------------
- Integrate new ways to Discover Templates (gitlab/github API)
- Frontend to interactively fill the template data


Usage
-----

Creating an API Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^
Every template endpoint requires 4 building blocks:

1. A Template Loader (Where can I find the templates? Which templates are available?)
2. The Template Environment (Settings for your Template)
3. A Global Provider (optional, global Variables available to all templates)
4. A compiler (optional, can perform actions on your rendered template)

As `flask-template-master` uses `Jinja2 <http://jinja.pocoo.org/>`_ under the hood, the first two pieces are provided by a "jinja Environment" object:

.. code-block:: python

    import jinja2
    from flask_template_master.environments import LATEX_TEMPLATE_CONFIG

    loader = jinja2.DictLoader({'a': '{{ test }}', 'b': '{{ test }} {{ global }}'})
    environment = jinja2.Environment(loader=loader, **LATEX_TEMPLATE_CONFIG)

The loader basically returns a list of available templates.
Jinja supports a variety of options, as documented `here <http://jinja.pocoo.org/docs/2.10/api/#loaders>`_.
You can also write your own loader using the existing ones as example.

The loader instance has to be passed into the environment.
The environment further handles things like the template config.
E.g. by default, jinja uses double curly braces ('{{ }}') to indicate variables in the template.
For certain file formats (e.g. LaTex) this might not be desirable and hence can be changed in the environment.
This package already provides some suitable configurations for certain scenarios under `flask_template_master.environments`
The example above uses the LaTex config.
However, you can configure the environment to your liking.
For example if you need to use custom functions in your templates, you would need to pass them into the environment (see `here <http://jinja.pocoo.org/docs/2.10/api/#high-level-api>`_).

The third important (but optional) component is the `Global Provider`.
While jinja has its own implementation of global variables, `flask-template-master` provides its own to give more granular control.
The Global Provider holds a set of global variables that are passed into context of each template.
`flask-template-master` provides different types of Global Providers depending on the source of your variables.
However, you can easily add your own (see below for further information).

.. code-block:: python

    from flask_template_master.global_provider import DictGlobalProvider

    global_provider = DictGlobalProvider({'global': 'This is a global value'})

The last (also optional parameter) is the compiler.
The compiler gets the fully rendered template text and can perform post-processing on it.
It is also trusted with building the response of the http request.
Hence, you can use the compiler to send the rendered text back as json object or provide it as file download, trigger side effects and more.
`flask-template-master` provides some compiler for common operations.
The most interesting is the LatexCompiler, which transpiles your template into an PDF and provides the PDF as file download.

.. code-block:: python

    from flask_template_master.compiler import LatexCompiler

    compiler = LatexCompiler()

Finally you need to combine all the building blocks to create a template endpoint.
This can either be done using a class based view:

.. code-block:: python

    from flask_template_master.views import BaseTemplateView

    class TestView(BaseTemplateView):
        ENVIRONMENT = environment
        GLOBAL_PROVIDER = global_provider
        COMPILER = compiler

    TestView.add_as_resource(api, '/class_test/')

or using the view factory function:

.. code-block:: python

    from flask_template_master.views import create_template_endpoint

    create_template_endpoint(api, '/factory_test/', environment=environment, compiler=compiler, global_provider=global_provider)

Both versions register a set of endpoints.
Taking the first one as example:

1. /class/test (GET): get the list of available templates
2. /class/test/a (GET): get information about the template named "a"
3. /class/test/a (POST): send variables to and render the template named "a"
4. /class/test/b (GET): get information about the template named "b"
5. /class/test/b (POST): send variables to and render the template named "b"

Note that both methods of registering the endpoints require an existing API instance.
This can be any existing flask-restfull Api instance.
This allows to incorporate the template endpoints as part of an existing larger REST API.

.. code-block:: python

    from flask_restfull import Api
    # or
    from flask_template_master import Api

    api = Api()  # create an instance of an flask-restfull API. Always required!

For a full project, see the example project folder.
You can use the provided Dockerfile (see docker folder) to run the example without installing the dependencies (in particular LaTex).


Installation
------------
.. code-block:: bash

    pip install flask-template-master

or if you want to develop an awesome new feature (yes, I know you want to!):

.. code-block:: bash

    git clone https://github.com/AKuederle/flask-template-master
    cd flask-template-master
    pip install -e .


Requirements
^^^^^^^^^^^^
See requirements.txt for dev requirements and setup.py for prod requirements

Licence
-------
`flask-template-master` is published under an MIT License.

Authors
-------

`flask-template-master` was written by `Arne Küderle <a.kuederle@gmail.com>`_.
