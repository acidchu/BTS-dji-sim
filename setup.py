# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="BTS-dji-sim",
    version="0.1.1",
    description="A simulated version of the dji robomaster library with some addons. Made for the bendigo tech school.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bendigo-tech-school/BTS-dji-sim",
    author="Bevan Matsacos",
    author_email="B.Matsacos@latrobe.edu.au",
    license="MIT",
    classifiers=[
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: Microsoft :: Windows :: Windows 11"
    ],
    packages=["BTS-dji-sim"],
    include_package_data=True,
)
