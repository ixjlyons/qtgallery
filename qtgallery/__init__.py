from .qtscraper import *
from ._version import __version__


def setup(app):
    from .qtgallery import setup
    return setup(app)
