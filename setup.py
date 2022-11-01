import os
import sys
from setuptools import setup
from io import open
from zappa import __version__

with open('README.md') as readme_file:
    long_description = readme_file.read()

with open(os.path.join(os.path.dirname(__file__), 'requirements.in')) as f:
    required = f.read().splitlines()

with open(os.path.join(os.path.dirname(__file__), 'test_requirements.in')) as f:
    test_required = f.read().splitlines()

setup(
    name='zappa',
    version=__version__,
    packages=['zappa'],
    install_requires=required,
    tests_require=test_required,
    test_suite='nose.collector',
    include_package_data=True,
    license='MIT License',
    description='Server-less Python Web Services for AWS Lambda and API Gateway',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Miserlou/Zappa',
    author='Rich Jones',
    author_email='rich@openwatch.net',
    entry_points={
        'console_scripts': [
            'zappa=zappa.cli:handle',
            'z=zappa.cli:handle',
        ]
    }
)
