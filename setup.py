import os
from setuptools import setup, find_packages

## This is a Python 3 package only
from sys import version_info
if version_info.major != 3:
    print("This package will only work with Python 3. \n"
          "If you already have Python 3 installed try 'pip3 install guizero'.")

__long_description__ = """# guizero

guizero is designed to allow new learners to quickly and easily create GUIs for their programs.

There is comprehensive documentation at [lawsie.github.io/guizero](https://lawsie.github.io/guizero/)

## Install

If you can download and unzip a file, you can [install guizero](https://lawsie.github.io/guizero/#easy-installation) - **no special permissions or administrator rights are required**.

If you have administrator rights and are connected to the internet, you can use [pip to quickly install guizero](#install-using-pip).

guizero only requires `tkinter` to be installed, which is included with a standard Python installation on all platforms except Linux.
A python module to allow learners to easily create GUIs. guizero is designed to be used by new learners. 

## Use

guizero is simple to use, taking away much of the complexity of creating simple GUIs.

```python
from guizero import App, Text
app = App(title="Hello world")
message = Text(app, text="Welcome to the Hello world app!")
app.display()
```

"""

setup(
    name="guizero",
    version="0.5.1",
    author="Laura Sach",
    author_email="laura.sach@raspberrypi.org",
    description="Python module to allow learners to easily create GUIs",
    long_description=__long_description__,
    long_description_content_type='text/markdown',
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
    install_requires=["pillow>=5"],
)
