from setuptools import setup, find_packages

setup(
    name='headergen',
    version='0.1.0',
    description='Generate a C header from a SystemRDL register definition',
    url='https://github.com/Julian-DD/SystemRDL-C-header',
    packages=find_packages(exclude=('test*')),
)