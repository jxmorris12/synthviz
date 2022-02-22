from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='synthviz',
    version='0.0.1',
    description='renders cool piano videos from file',
    long_description_content_type='text/markdown',
    long_description=long_description,
    author='Jack Morris',
    author_email='jxmorris12@gmail.com',
    url='https://github.com/jxmorris12/synthviz',
    license='GNU GPL',
    packages=find_packages(),
    install_requires=open('requirements.txt').readlines(),
)

