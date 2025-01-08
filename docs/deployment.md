# Deploy

Notes on how to deploy guizero (on Windows).

## Prepare

- Update version number in `guizero\__init__.py`
- Update version number in `docs-src\docs\about.md`
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

## Promote and tag release on github

- Push all changes to `master`.
- Create a new release on github named `0.0.0`. 
