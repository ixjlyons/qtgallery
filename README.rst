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

``qtgallery`` enables sphinx-based documentation to include screenshots of Qt
applications, with most functionality provided by `sphinx-gallery`_.

The `docs`_ themselves serve as a demonstration of what the library does.

The library itself uses `QtPy`_ to support all Python Qt bindings, meaning your
examples can use any bindings you want (i.e. PySide{2,6}, PyQt{5,6}).
Ultimately, you only need to specify a particular flavor in the sphinx build
environment.

Currently, ``qtgallery`` depends on ``Xvfb`` for headless rendering, restricting
it to Linux for headless usage.


Installation
============

``qtgallery`` is available on PyPI_, so it can be installed with pip::

    $ pip install qtgallery

To try out the repository and get a feel for how it is configured, clone the
repository and install a few extra requirements to build the documentation
locally::

    $ git clone git@github.com:ixjlyons/qtgallery.git
    $ cd qtgallery/docs
    $ pip install -r requirements.txt
    $ make html

Open up ``docs/_build/html/index.html`` to see built docs. They're currently
being hosted by Read the Docs as well:

https://qtgallery.readthedocs.io/


Configuration
=============

To use ``qtgallery`` in your own documentation, start by setting up a normal
`sphinx-gallery`_ -- `qtgallery`` essentially is a library to make standalone Qt
application scripts work within a sphinx-gallery. Setting up a simple matplotlib
example to get started might be a good idea.

Next, add ``qtgallery`` to ``extensions``:

.. code-block:: python

   # sphinx conf.py
   extensions = {
       "sphinx_gallery.gen_gallery",
       "qtgallery",
       ...
    }

Next, add the ``qtgallery`` `image scraper`_ and `reset function`_ to
``sphinx_gallery_conf`` as follows:

.. code-block:: python

   # sphinx conf.py
   import qtgallery

   sphinx_gallery_conf = {
       'image_scrapers': (qtgallery.qtscraper, ...),
       'reset_modules': (qtgallery.reset_qapp, ...),
       ...
   }

Note that you can use additional scrapers and reset modules if needed. The docs
for ``qtgallery`` also use the "matplotlib" scraper, for example.

The ``qtscraper`` is responsible for generating renderings of all currently
shown top level windows within the scope of the example.

The reset module is for handling ``QApplication``, allowing you to instantiate
the ``QApplication`` singleton in each example and preventing the Qt event loop
from running and hanging the docs build. That is, examples that run ok standalone
should behave ok in generating the gallery as well.

Display Configuration
---------------------

The ``qtgallery_conf`` sphinx configuration variable can be used to configure
the virtual display used. Default settings are listed below (see also
``qtgallery/__init__.py``). The values are passed along in constructing a
PyVirtualDisplay_ ``Display``:

.. code-block:: python

   # sphinx conf.py
   qtgallery_conf = {
        "xvfb_size": (640, 480),
        "xvfb_color_depth": 24,
        "xfvb_use_xauth": False,
        "xfvb_extra_args": [],
    }

Troubleshooting note: if you find that the rendered screenshots "cut off" some
contents of your application compared to when they're run normally, try
increasing ``xvfb_size``.


Usage
=====

Usage pretty much follows `sphinx-gallery`_, but one tip is that you can control
*where* the window is displayed in the context of a "tutorial style" example via
``show()``.  See the `iterative example`_ to see how this works.

Read the Docs
-------------

On Read the Docs, ``xvfb`` is required. See their documentation for `installing
apt packages`_. This repository also serves as an example (see
``.readthedocs.yml``).

CI
--

Similar to Read the Docs, getting ``qtgallery`` working in a CI environment like
GitHub Actions will likely require some additional dependencies.

``qtgallery`` itself uses GitHub actions for testing, so take a look at the
``tests`` action to see the Ubuntu packages being installed. This should be a
good starting point for using ``qtgallery`` with GitHub Pages, for example.


.. _sphinx-gallery: https://sphinx-gallery.github.io/stable/index.html
.. _docs: https://qtgallery.readthedocs.io/en/latest/auto_examples/index.html 
.. _QtPy: https://github.com/spyder-ide/qtpy
.. _PyPI: https://pypi.org/project/qtgallery/
.. _image scraper: https://sphinx-gallery.github.io/stable/configuration.html#image-scrapers
.. _reset function: https://sphinx-gallery.github.io/stable/configuration.html#resetting-modules
.. _PyVirtualDisplay: https://github.com/ponty/PyVirtualDisplay
.. _iterative example: https://qtgallery.readthedocs.io/en/latest/auto_examples/iterative.html#sphx-glr-auto-examples-iterative-py
.. _installing apt packages: https://docs.readthedocs.io/en/stable/config-file/v2.html#build-apt-packages
.. _GitHub Pages: https://pages.github.com/
