# Development

Notes on how to develop guizero (on Windows).

## Install Pre-requisites

```
pip install mkdocs
pip install wheel
pip install twine
pip install virtualenv
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

## Documents

Test documents by serving up MkDocs:

```
cd guizero\docs-src
mkdocs serve
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) 
