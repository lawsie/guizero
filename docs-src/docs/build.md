# Development and Deployment

Notes on how to develop and deploy guizero (on Windows).

## Development

### Install Pre-requisites

Install MkDocs

```
pip install mkdocs
```

### Python library

Checkout and install guizero for development:

```
git clone https://github.com/lawsie/guizero
cd guizero
git checkout dev
python setup.py develop
```

### Documents

Test documents by serving up MkDocs:

```
cd guizero\docs-src
mkdocs serve
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) 

## Deploy

### Python library

Install locally:

```
cd guizero
python setup.py install
```

Build for deployment:

```
cd guizero
python setup.py sdist
python setup.py bdist_wheel
```

Upload to pypi:

```
cd guizero
twine upload dist/* --skip-existing
```

### Documents

Build:

```
cd guizero/docs-src
mkdocs build
```

Copy to `docs`:

```
xcopy guizero/docs-src/site/* guizero/docs
```
