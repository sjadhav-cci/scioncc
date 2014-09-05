#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

import os
import sys

# Add /usr/local/include to the path for macs, fixes easy_install for several packages (like gevent and pyyaml)
if sys.platform == 'darwin':
    os.environ['C_INCLUDE_PATH'] = '/usr/local/include'

version = '0.0.1-dev'

setup(  name = 'scion',
        version = version,
        description = 'Scientific Observatory Network',
        url = '',
        download_url = '',
        license = 'BSD',
        author = '',
        author_email = '',
        keywords = ['scion','pyon'],
        packages = find_packages(),
        entry_points = {
            'console_scripts' : [
                'pycc=scripts.pycc:entry',
                'control_cc=scripts.control_cc:main',
                'generate_interfaces=scripts.generate_interfaces:main',
                'store_interfaces=scripts.store_interfaces:main',
                'clear_db=pyon.datastore.clear_couch_util:main',
                ]
            },
        dependency_links = [
            'http://sddevrepo.oceanobservatories.org/releases/',
            'https://github.com/ooici/utilities/tarball/v2013.06.11#egg=utilities-2013.06.11',
        ],
        test_suite = 'pyon',
        package_data = {'': ['*.xml']},
        install_requires = [
            'utilities',
            'greenlet==0.4.0',
            # Don't put == version on gevent
            'gevent',
            'simplejson',
            'msgpack-python==0.1.13',
            'pika==0.9.5',
            'httplib2>=0.7.2',
            'pyzmq==2.2.0',
            'gevent_zeromq==0.2.5',
            'zope.interface',
            'couchdb==0.9',
            'psycopg2',
            'python-daemon==1.6',
            'M2Crypto',
            'nose==1.1.2',
            'ipython==0.13.0',
            'antlr_python_runtime==3.1.3',
            'readline',
            'mock==0.8',
            'ndg-xacml==0.5.1',
            'python-gevent-profiler',
            'lxml',
            'requests',
            'psutil',
            'Flask',
            'python-dateutil',
            'pyparsing==1.5.6',
            'ntplib',
            'xlrd',
            'xlwt',
        ],
     )
