# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='doodles',
    version='0.1.0',
    description='Rick\'s Math Doodles',
    long_description=readme,
    author='Richard S Kawala',
    author_email='rkawala@gmail.com',
    url='https://github.com/rkawala/math-doodles',
    license=license,
    packages=find_packages(exclude=('tests'))
)

