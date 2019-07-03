import os
import pathlib
from setuptools import setup, find_packages

install_requires = [
	'setuptools',
	'ZODB',
	'zope.interface',
	'transaction',
]

entry_points = """
"""

# The directory containing this file
HERE = pathlib.Path(__file__).parent
name, version = 'ZODBuffer', '1.0.1'
description="ZODB Database file splitter",
url="https://github.com/qpaycm/ZODBuffer",

setup(
    author='vir2alexport',
    author_email='vir2alexport@gmail.com',
    license='MIT',
    name=name, version=version,
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
    ],
    packages=[name],
    package_dir={'':'src'},
    install_requires=install_requires,
    zip_safe=False,
    entry_points=entry_points,
    include_package_data=True,
)
