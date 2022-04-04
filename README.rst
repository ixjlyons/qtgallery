=========
qtgallery
=========

.. image:: https://badge.fury.io/py/qtgallery.svg
   :target: https://badge.fury.io/py/qtgallery
   :alt: PyPI Package

.. image:: https://readthedocs.org/projects/qtgallery/badge/?version=latest
   :target: https://qtgallery.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://github.com/ixjlyons/qtgallery/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/ixjlyons/qtgallery/actions?workflow=Tests
   :alt: Tests

.. image:: https://codecov.io/gh/ixjlyons/qtgallery/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/ixjlyons/qtgallery
   :alt: Codecov


Scraper for generating a `sphinx-gallery`_ of Qt windows.

This repository serves both as a library for grabbing renderings of Qt windows
to add to your own ``sphinx-gallery`` config as well as an example of its usage.


Installation
============

``qtgallery`` is available on PyPI_, so it can be installed with pip::

    $ pip install qtgallery

To try out the repository and get a feel for how it is configured, clone the
repository and install a few extra requirements to build the documentation
locally::

    $ git clone git@github.com:ixjlyons/qtgallery.git
    $ cd qtgallery/docs
    $ pip install -r requirements
    $ make html

Open up ``docs/_build/html/index.html`` to see built docs. They're currently
being hosted by Read the Docs as well:

https://qtgallery.readthedocs.io/


Configuration
=============

To use ``qtgallery`` in your own documentation, start by setting up
`sphinx-gallery`_ -- ``qtgallery`` doesn't have its own configuration and
instead relies on ``sphinx_gallery_conf``. Setting up a simple matplotlib plot
as an example might be a good idea for testing the configuration works.

Next, add ``qtgallery`` to ``extensions``:

.. code-block:: python

   # sphinx conf.py
   extensions = {
       ...
       'sphinx_gallery.gen_gallery',
       'qtgallery',
    }

Next, add the ``qtgallery`` `image scraper`_ and `reset function`_ to
``sphinx_gallery_conf`` as follows:

.. code-block:: python

   # sphinx conf.py
   import qtgallery

   sphinx_gallery_conf = {
       ...
       'image_scrapers': (qtgallery.qtscraper, ...),
       'reset_modules': (qtgallery.reset_qapp, ...),
   }

The image scraper is responsible for generating a rendering of all currently
shown top level windows.

The reset function is for handling ``QApplication``, allowing you to instantiate
the ``QApplication`` singleton in each example and preventing the Qt event loop
from running and hanging the docs build. That is, examples that run ok standalone
should behave ok in generating the gallery.


Usage
=====

Usage pretty much follows `sphinx-gallery`_, but one tip is that you can control
*where* the window is rendered via ``show()``. See the `iterative
example`_ to see how this works.

Read the Docs
-------------

On Read the Docs, ``xvfb`` is required. See their documentation for `installing
apt packages`_. This repository also serves as an example (see
``.readthedocs.yml``).


.. _sphinx-gallery: https://sphinx-gallery.github.io/stable/index.html
.. _PyPI: https://pypi.org/project/qtgallery/
.. _image scraper: https://sphinx-gallery.github.io/stable/configuration.html#image-scrapers
.. _reset function: https://sphinx-gallery.github.io/stable/configuration.html#resetting-modules
.. _iterative example: https://qtgallery.readthedocs.io/en/latest/auto_examples/iterative.html#sphx-glr-auto-examples-iterative-py
.. _installing apt packages: https://docs.readthedocs.io/en/stable/config-file/v2.html#build-apt-packages
