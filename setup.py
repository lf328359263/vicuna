# -*- coding: UTF-8 -*-
import io
from setuptools import find_packages
from setuptools import setup

with io.open("README.md", "md", encoding="utf8") as f:
    readme = f.read()

setup(
    name='vicuna',
    version='1.0.0',
    url='http://localhost:5000/docs/tutorial',
    license='BSD',
    maintainer='kongxiangshuai',
    maintainer_email='kongxiangshuai@example.com',
    description='cluster deploy and management',
    long_description=readme,
    packages=find_packages(),
    # packages=['vicuna'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['flask'],
    extras_require={'test': ['pytest', 'coverage']},
)