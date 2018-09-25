# Cracking the Coding Interview (6th Edition)
Just me working through a coding interview book.

## Developing

### Dependencies
```bash
brew install python pipenv # Note that `brew install python` now installs Python 3

# Install all dependencies (including dev dependencies) as described in Pipfile (and Pipfile.lock)
# Extend the timeout for venv creation, as this can take awhile
PIPENV_TIMEOUT=600 pipenv install --dev
```

And to add more Python dependencies:
```bash
pipenv install <package> # i.e. pipenv install beautifulsoup4==4.6.*
pipenv install --dev <dev-package> # i.e. pipenv install --dev pytest==3.8.*
```

### Workflow
```bash
pipenv shell # activate virtualenv
pytest -v # run tests, verbose output
mypy main.py # check types >>> TODO: make this work without main.py
exit # deactivate virtualenv
```
