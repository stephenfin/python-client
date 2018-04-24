#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup
import re
import os
import sys


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version('coreapi')


if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist bdist_wheel upload")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()


setup(
    name='coreapi',
    version=version,
    url='https://github.com/core-api/python-client',
    license='BSD',
    description='Python client library for Core API.',
    author='Tom Christie',
    author_email='tom@tomchristie.com',
    packages=find_packages('coreapi'),
    include_package_data=True,
    install_requires=[
        'coreschema',
        'requests',
        'itypes',
        'uritemplate'
    ],
    entry_points={
        'coreapi.codecs': [
            'corejson=coreapi.codecs:CoreJSONCodec',
            'json=coreapi.codecs:JSONCodec',
            'text=coreapi.codecs:TextCodec',
            'download=coreapi.codecs:DownloadCodec',
        ],
        'coreapi.transports': [
            'http=coreapi.transports:HTTPTransport',
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
