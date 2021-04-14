# -*- coding: utf-8 -*-

#  marketholidays.py
#  -----------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of marketholidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  MichealOmojola <momojola@aust.edu.ng>
#  Website: https://github.com/OmoMicheal/trading_days
#  License: MIT (see LICENSE file)
#  Version: 0.1 (April 7, 2021)



try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    

setup(
    name='marketanalysis',
    packages = ['marketanalysis'],
    version='0.1',
    author='Micheal Omojola',
    description='A repository for market holidays and trading days in NYSE and NASDAQ',
    download_url = 'https://github.com/OmoMicheal/marketanalysis/archive/refs/tags/0.1.tar.gz',
    author_email='momojola@aust.edu.ng',
    url='https://github.com/OmoMicheal/marketanalysis',
    bugtrack_url='https://github.com/OmoMicheal/marketanalysis/issues',
    license='MIT License',
    py_modules=['marketanalysis'],
    keywords = ['trading', 'NYSE', 'NASDAQ','market holidays','trading days'],
    long_description=open('README.rst', encoding='utf-8').read(),
    long_description_content_type = 'text/x-rst',
    install_requires=['datetime','python-dateutil','six'],    
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Office/Business :: Scheduling',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Localization',
    ],
)




