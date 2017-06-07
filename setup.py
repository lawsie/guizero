import os
from setuptools import setup, find_packages

## This is a Python 3 package only
from sys import version_info
if version_info.major != 3:
    print("This package will only work with Python 3. \n" 
          "If you already have Python 3 installed try 'pip3 install guizero'.")

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="guizero",
    version="0.3.3",
    author="Laura Sach",
    author_email="laura.sach@raspberrypi.org",
    description="Python module to allow kids to easily create GUIs",
    long_description=read('README.rst'),
    license="BSD",
    keywords=[
        "GUI",
        "GUIzero",
        "interface",
    ],
    url="https://github.com/lawsie/guizero",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Topic :: Education",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Education",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
    ],
)
