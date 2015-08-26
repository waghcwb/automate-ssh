import os
from setuptools import setup

setup(
    name = 'AutomateSSH',
    version = '0.0.1',
    author = 'waghcwb',
    author_email = 'wagh.cwb@gmail.com',
    description = (
        'Automate SSH tasks with Python'
    ),
    license = 'GNU',
    keywords = 'automate ssh python tasks',
    url = 'https://github.com/waghcwb/automate-ssh',
    install_requires = [
        'paramiko'
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities'
    ],
)