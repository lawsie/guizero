import os
from setuptools import setup, find_packages

## This is a Python 3 package only
from sys import version_info
if version_info.major != 3:
    print("This package will only work with Python 3. \n"
          "If you already have Python 3 installed try 'pip3 install guizero'.")

setup(
    name="guizero",
    version="0.4.1",
    author="Laura Sach",
    author_email="laura.sach@raspberrypi.org",
    description="Python module to allow kids to easily create GUIs",
    long_description="""guizero is designed to be used by children. In educational settings,
installation of extra programs and features may be difficult, so the set up
process is designed to be as simple as possible.""",
    license="BSD",
    keywords=[
        "GUI",
        "guizero",
        "interface",
    ],
    url="https://github.com/lawsie/guizero",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Topic :: Education",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Education",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
    ],
)
