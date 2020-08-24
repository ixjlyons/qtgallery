from setuptools import setup

setup(
    name='qtgallery',
    version='0.0.1',
    description='sphinx-gallery scraper for Qt examples and tutorials',
    author='Kenneth Lyons',
    author_email='ixjlyons@gmail.com',
    license='MIT',
    packages=['qtgallery'],
    install_requires=['pyside2', 'qtpy', 'sphinx', 'sphinx-gallery', 'pillow',
                      'sphinx_rtd_theme'],
)
