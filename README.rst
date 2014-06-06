===============================
nose-htmloutput
===============================


.. image:: http://img.shields.io/travis/ionelmc/nose-htmloutput/master.png
    :alt: Build Status
    :target: https://travis-ci.org/ionelmc/nose-htmloutput

.. image:: http://img.shields.io/coveralls/ionelmc/nose-htmloutput/master.png
    :alt: Coverage Status
    :target: https://coveralls.io/r/ionelmc/nose-htmloutput

.. image:: http://img.shields.io/pypi/v/nose-htmloutput.png
    :alt: PYPI Package
    :target: https://pypi.python.org/pypi/nose-htmloutput

.. image:: http://img.shields.io/pypi/dm/nose-htmloutput.png
    :alt: PYPI Package
    :target: https://pypi.python.org/pypi/nose-htmloutput

Nose plugin that generates a nice html test report.

* Free software: BSD license

Installation
============

::

    pip install nose-htmloutput

Usage
=====

  --with-html           Enable plugin HtmlOutput:  Output test results as
                        pretty html.  [NOSE_WITH_HTML]
  --html-file=FILE      Path to html file to store the report in. Default is
                        nosetests.html in the working directory

Development
===========

To run the all tests run::

    tox

Example
=======

.. image:: docs/sample.png

.. image:: sample.png
