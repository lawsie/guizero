# Deploy

Notes on how to deploy guizero (on Windows).

## Prepare

- Update version number in `setup.py`
- Update version number in `README.md`
- Update release date in `README.md`
- Update version number in `docs-src\docs\about.md`
- Update `changelog` in debian packages
- Update `changelog.md` in docs

## Python library

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

Create .pypirc credentials:

```
cd %HOME%
notepad .pypirc
```

```
[distutils]
index-servers =
    pypi

[pypi]
username:
password:
```

Upload to pypi:

```
cd guizero
twine upload dist/* --skip-existing
```

## Documents

Build:

```
cd guizero/docs-src
mkdocs build
```

Copy to `docs`:

```
cd guizero
xcopy docs-src\site\* docs /E
```
