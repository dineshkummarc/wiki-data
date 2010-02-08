# YOU NEED TO EDIT THESE
AUTHOR = 'Wiki-Data'
AUTHOR_EMAIL = 'suppoert@wiki-data.com'
NAME = 'tiddlywebplugins.wikidata'
DESCRIPTION = 'Packaging of Wiki-Data Project'
VERSION = '0.31'


import os

from setuptools import setup, find_packages


# You should carefully review the below (install_requires especially).
setup(
    namespace_packages = ['tiddlywebplugins'],
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    long_description = open(os.path.join(os.path.dirname(__file__), 'README')).read(),
    author = AUTHOR,
    url = 'http://pypi.python.org/pypi/%s' % NAME,
    packages = find_packages(exclude='test'),
    author_email = AUTHOR_EMAIL,
    platforms = 'Posix; MacOS X; Windows',
    install_requires = ['setuptools',
        'tiddlyweb',
        'tiddlywebplugins.utils',
        'tiddlywebplugins.diststore',
        'tiddlywebplugins.methodhack',
        'tiddlywebplugins.templates',
        'tiddlywebplugins.logout',
        'tiddlywebplugins.mappingsql',
        ],
    zip_safe = False,
    include_package_data = True,
    )
