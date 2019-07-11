import os
from setuptools import setup, find_packages
from guizero import __name__, __package__, __version__, __author__

## This is a Python 3 package only
from sys import version_info
if version_info.major != 3:
    print("This package will only work with Python 3. \n"
          "If you already have Python 3 installed try 'pip3 install guizero'.")

__desc__ = 'Python module to allow learners to easily create GUIs'
__author_email__ = 'laura.sach@raspberrypi.org'
__license__ = 'BSD'
__url__ = 'https://github.com/lawsie/guizero'
__requires__ = []
__extras_require__={
        'images':  ["pillow>=4.3.0"]
    }
__python_requires__ = ">=3"
__keywords__ = [
    "GUI",
    "guizero",
    "interface",
]
__classifiers__ = [
    "Development Status :: 5 - Production/Stable",
    "Programming Language :: Python :: 3",
    "Topic :: Education",
    "Topic :: Software Development :: User Interfaces",
    "Topic :: Education",
    "Intended Audience :: Education",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
]
__long_description__ = """# guizero

guizero is designed to allow new learners to quickly and easily create GUIs for their programs.

There is comprehensive documentation at [lawsie.github.io/guizero](https://lawsie.github.io/guizero/)

## Install

If you can download and unzip a file, you can [install guizero](https://lawsie.github.io/guizero/#easy-install) - **no special permissions or administrator rights are required**.

If you have administrator rights and are connected to the internet, you can use [pip to quickly install guizero]((https://lawsie.github.io/guizero/#install-using-pip).

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
    name=__name__,
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    description=__desc__,
    long_description=__long_description__,
    long_description_content_type='text/markdown',
    license=__license__,
    keywords=__keywords__,
    url=__url__,
    packages=find_packages(),
    classifiers=__classifiers__,
    install_requires=__requires__,
    extras_require = __extras_require__,
    python_requires=__python_requires__,
)
