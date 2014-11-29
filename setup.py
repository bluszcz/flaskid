#from distutils.core import setup
from setuptools import setup

setup(
    # Application name:
    name="FlaskId",

    # Version number (initial):
    version="0.0.0-dev",

    # Application author details:
    author="Rafal bluszcz Zawadzki",
    author_email="bluszcz@bluszcz.net",

    # Packages
    packages=["flaskid"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="http://pypi.python.org/pypi/FlaskId_v010/",

    #
    license="LICENSE",
    description="Flask based OpenID server implementation.",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        open("requirements.txt").readlines(),
    ],
)