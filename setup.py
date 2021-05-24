import os
import codecs
from setuptools import setup


def read(fp):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, fp), 'r') as f:
        return f.read()


exec(read(os.path.join("qtgallery", "_version.py")))

setup(
    name="qtgallery",
    version=__version__,
    description="sphinx-gallery scraper for Qt examples and tutorials",
    long_description=read("README.rst"),
    author="Kenneth Lyons",
    author_email="ixjlyons@gmail.com",
    license="MIT",
    packages=["qtgallery"],
    install_requires=[
        "qtpy",
        "pyvirtualdisplay",
        "sphinx_gallery",
        "pillow",
        "sphinx_rtd_theme",
    ],
)
