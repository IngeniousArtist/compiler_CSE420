# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='compiler_CSE420',
    version='0.1.0',
    description='Project work for Compiler Design Course at BRAC University.',
    long_description=readme,
    author='Mohammad Muhtasim Shahriyer',
    author_email='ingeniousartist@gmail.com',
    url='https://github.com/IngeniousArtist/compiler_CSE420',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)