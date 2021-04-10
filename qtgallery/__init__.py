from .qtscraper import *

__version__ = "0.1.0"


def setup(app):
    from .qtgallery import setup
    return setup(app)
