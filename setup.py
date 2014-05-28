# -*- encoding: utf8 -*-
from setuptools import setup, find_packages

import os
import re
import io


def read(*names, **kwargs):
    return io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()

setup(
    name="nose-htmloutput",
    version="0.1",
    url='https://github.com/ionelmc/nose-htmloutput',
    download_url='',
    license='BSD',
    description="...",
    long_description=read('README.rst'),
    author='Ionel Cristian Mărieș',
    author_email='contact@ionelmc.ro',
    py_modules=['nose_htmloutput'],
    package_dir={'': 'src'},
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    keywords=[
    ],
    install_requires=[
        'Jinja2',
    ],
    extras_require={
    },
    entry_points = {
        'nose.plugins.0.10': [
            'html = nose_htmloutput:HtmlOutput'
        ]
    }
) 
