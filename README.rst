=========
qtgallery
=========

.. image:: https://readthedocs.org/projects/qtgallery/badge/?version=latest
   :target: https://qtgallery.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

Scraper for generating a `sphinx-gallery`_ of Qt widgets.

This repository serves both as a library for grabbing renderings of Qt widgets
to add to your own ``sphinx-gallery`` config as well as an example of its usage.


Installation
============

For the time being, clone the repo and install from source::

    $ git clone git@github.com:ixjlyons/qtgallery.git
    $ cd qtgallery
    $ pip install .

Now you should be able to generate the docs/gallery::

    $ cd doc
    $ make html

Open up ``doc/_build/html/index.html`` to see built docs. They're currently
being hosted by Read the Docs as well:

https://qtgallery.readthedocs.io/


Configuration
=============

To use ``qtgallery`` in your own documentation, start by setting up
`sphinx-gallery`_. This library provides two key components to add to your
``sphinx_gallery_conf``: an `image scraper`_ and a `reset function`_:

.. code-block:: python

   # sphinx conf.py
   import qtgallery

   sphinx_gallery_conf = {
       ...
       'image_scrapers': (qtgallery.qtscraper, ...),
       'reset_modules': (qtgallery.reset_qapp, ...),
       ...
   }

The image scraper is responsible for generating a rendering of all currently
shown top level widgets.

The reset function is for handling ``QApplication``, allowing you to instantiate
the ``QApplication`` singleton in each example and preventing the Qt event loop
from running and hanging the docs build. That is, examples that run ok standalone
should behave ok in generating the gallery.


Usage
=====

Usage pretty much follows `sphinx-gallery`_, but one tip is that you can control
*where* the widget/window is rendered via ``show()``. See the `iterative
example`_ to see how this works.

Read the Docs
-------------

On Read the Docs, ``xvfb`` is required. See their documentation for `installing
apt packages`_. This repository also serves as an example (see
``.readthedocs.yml``).


.. _sphinx-gallery: https://sphinx-gallery.github.io/stable/index.html
.. _image scraper: https://sphinx-gallery.github.io/stable/configuration.html#image-scrapers
.. _reset function: https://sphinx-gallery.github.io/stable/configuration.html#resetting-modules
.. _iterative example: https://qtgallery.readthedocs.io/en/latest/auto_examples/iterative.html#sphx-glr-auto-examples-iterative-py
.. _installing apt packages: https://docs.readthedocs.io/en/stable/config-file/v2.html#build-apt-packages
