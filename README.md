# Cracking the Coding Interview (6th Edition)
Just me working through a coding interview book.

## Developing

### Dependencies
```bash
brew install python pipenv # Python 3
pipenv install # install Python dependencies
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
