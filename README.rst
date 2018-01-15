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
