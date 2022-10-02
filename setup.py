#!/usr/bin/env python
import pathlib

from setuptools import setup

readme = pathlib.Path(pathlib.Path(__file__).parent / "README.md").read_text()

setup(
    name="django-pwny",
    version="0.2.0",
    description="Have I Been Pwned? password validator",
    long_description=readme,
    author="PsypherPunk",
    author_email="psypherpunk@gmail.com",
    url="https://github.com/PsypherPunk/django-pwny",
    packages=["pwny"],
    include_package_data=True,
    install_requires=[],
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords="django-pwny",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License"
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
)
