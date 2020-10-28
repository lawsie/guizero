# Development

Notes on how to develop guizero (on Windows).

## Setup

Upgrade pip:

```
python.exe -m pip install pip --upgrade
```

Install / upgrade pre-requisites:

```
pip install mkdocs wheel twine virtualenv pytest pillow --upgrade
```

## Python library

Create a virtual environment (not essential, but a good idea!):

```
virtualenv guizero-[versionno]
cd guizero-[versionno]
```

Activate your virtual environment:

```
Scripts\activate
```

Checkout and install guizero for development:

```
git clone https://github.com/lawsie/guizero
cd guizero
git checkout dev
python setup.py develop
```

When you have finished your development, deactivate your virtual environment:

```
Scripts\deactivate
```

## Tests

To run the automated tests:

```
cd guizero\test
pytest -v
```

If running the tests inside a virtual environment you will need to install pytest in that virtual environment.

```
pip install pytest
```

_Note - tkinter can error when running the tests usually when the interpreter doesn't start properly, it doesn't seem to like being initialised and destroyed hundreds of times, I suspect a file locking issue as you don't see the problem on Linux. So sometimes you might get a test fail with an error like `This probably means that tk wasn't installed properly.`. Just re-run the last failed errors! `pytest --lf -v`_

## Documents

Test documents by serving up MkDocs:

```
cd guizero\docs-src
mkdocs serve
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
