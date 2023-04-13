from setuptools import setup, find_packages

setup(
    name='ralbot',
    version='1.1.0',
    description='Generate a C header from a SystemRDL register definition',
    url='https://github.com/Julian-DD/SystemRDL-C-header',
    packages=find_packages(),
    install_requires=['peakrdl']
)
