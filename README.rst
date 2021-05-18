=========
qtgallery
=========

.. image:: https://readthedocs.org/projects/qtgallery/badge/?version=latest
   :target: https://qtgallery.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

This is a work-in-progress demo as I try to figure out how to get
`sphinx-gallery`_ to render screenshots of Qt applications.

To test, make a virtual environment, then install the package::

    $ python -m venv .venv
    $ source .venv/bin/activate[.fish]
    (.venv) $ pip install .

Now you should be able to generate the docs/gallery::

    (.venv) $ cd doc
    (.venv) $ make html

Open up ``doc/_build/html/index.html`` to see built docs.

.. _sphinx-gallery: https://sphinx-gallery.github.io/stable/index.html
