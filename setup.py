import os
from setuptools import setup, find_packages

setup(
    name="guizero",
    version="0.2.1",
    author="Laura Sach",
    author_email="laura.sach@raspberrypi.org",
    description="Python module to allow kids to easily create GUIs",
    long_description=open('README').read(),
    license="BSD",
    keywords=[
        "GUI",
        "GUIzero",
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
