# TDR prototype REST API

A REST API for the Transfer Digital Records prototype.

**This repository has been retired.** It was a prototype that was built during
the [Transfer Digital Records](https://github.com/nationalarchives/tdr-dev-documentation/)
Alpha phase.

## Developer setup

Install Python 3 and make sure you can run it using the command `python3`.
[pyenv] is a good option if Python 3 is not installed on your system by default.

[pyenv]: https://realpython.com/intro-to-pyenv/

Start a python virtual environment:
```
python3.6 -m venv venv/
source venv/bin/activate
pip install -r requirements.txt

````
Install development dependencies with:

```
yarn install
pip install -r requirements.txt
```

Run the API:

```
yarn offline --stage=local --port=3001
```
