import setuptools

setuptools.setup(
    name="flask-template-master",
    version="0.1.0",
    url="https://github.com/AKuederle/flask-template-master",

    author="Arne Küderle",
    author_email="a.kuederle@gmail.com",

    description="A flask plugin to create a template render service",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "test*"]),

    install_requires=['flask', 'flask_restful', 'jinja2'],

    license='LICENSE',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3.5',
    ],
)
