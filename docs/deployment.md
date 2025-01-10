# Deploy

Notes on how to deploy guizero (on Windows).

## Prepare

- Update version number in `guizero\__init__.py`
- Update version number in `docs\about.md`
- Update `changelog.md` in docs
- Update version number in `pyproject.toml` 

## Python library

Install locally:

```
cd guizero
python setup.py install
```

Build for deployment:

```
cd guizero
python -m build
```

Upload to pypi:

```
cd guizero
twine upload dist/* --skip-existing
```

## Documents

Build:

```
cd guizero/docs
mkdocs build
```

Deploy:

```
cd guizero
mkdocs gh-deploy
```

## Promote and tag release on github

- Push all changes to `master`.
- Create a new release on github named `0.0.0`. 
