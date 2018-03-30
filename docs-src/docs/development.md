# Development

Notes on how to develop guizero (on Windows).

## Install Pre-requisites

```
pip install mkdocs wheel twine virtualenv pytest pillow
```

## Python library

Create a virtual environment (not essential, but a good idea!):

```
mkdir guizero-[versionno]
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

_Note - tkinter can error when running the tests usually when the interpreter doesn't start properly, it doesnt seem to like being initialised and destroyed hundreds of times, I suspect a file locking issue as you dont see the problem on Linux. So sometimes you might get a test fail with an error like `This probably means that tk wasn't installed properly.`._

_Just give it a re-run!_

## Documents

Test documents by serving up MkDocs:

```
cd guizero\docs-src
mkdocs serve
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) 
