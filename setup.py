"""
Flask-Bootstrap
===============

Flask-Bootstrap packages `Twitter's Bootstrap
<http://twitter.github.com/bootstrap/>`_ into an extension that mostly consists
of a blueprint named 'bootstrap'.

Usage
-----
``
from flask.ext.bootstrap import Bootstrap

[...]

Bootstrap(app)
``

This makes some new templates available, mainly `bootstrap_base.html` and
`bootstrap_responsive.html`. These are blank pages that include all bootstrap
resources, and have predefined blocks where you can put your content. The core
block to alter is `body_content`, otherwise see the source of the template for
more possiblities.

The url-endpoint `bootstrap.static` is available for refering to Bootstrap
resources, but usually, this isn't needed.

Configuration options
---------------------
There are a few configuration options used by the templates:

* `BOOTSTRAP_USE_MINIFIED` (default: True) - whether or not to use the
  minified versions of the css/js files
* `BOOTSTRAP_JQUERY_VERSION` (default: '1.7.2') - this version of jQuery is
* included in the template via Google CDN. Also honors
  `BOOTSTRAP_USE_MINIFIED`. Set this to `None` to not include jQuery at all.
* `BOOTSTRAP_HTML5_SHIM`. Include the default IE-fixes that are usually
  included when using bootstrap.
"""
from setuptools import setup


setup(
    name='Flask-Bootstrap',
    version='2.0.3-1',
    url='http://github.com/mbr/flask-bootstrap',
    license='BSD',
    author='Marc Brinkmann.de',
    author_email='git@marcbrinkmann.de',
    description='An extension that includes Twitter\'s Bootstrap in your '
                'project, without any boilerplate code.',
    long_description=__doc__,
    packages=['flask_bootstrap'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.8'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
