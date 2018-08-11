# Starter repo for python modules
[![CircleCI](https://circleci.com/gh/AumitLeon/module_starter_cli.svg?style=svg)](https://circleci.com/gh/AumitLeon/module_starter_cli) [![PyPI version](https://badge.fury.io/py/module-starter.leon.svg)](https://badge.fury.io/py/module-starter.leon)
[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/semantic-release/semantic-release)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)

This project is preconfigured with [circleci](https://circleci.com/), and serves as the starting point for the development and deployment of future Python modules that automate releases via `semantic-release.`

## Usage
To create a module while using this repo as a template, create a new repo, and set this project as the remote upstream. This means that when you `git fetch` and `git merge`, your module project will be updated with changes made in this starter project. 

To set the upstream of your project: 
```
git remote add upstream git@github.com:AumitLeon/module_starter_cli.git
```

Keeping your downstream modules synced with this project is important because breaking changes made here should be reflected in all subsequent projects.

## Installation
To install this module:
```
pip install module-starter.leon
```
Downstream modules can be installed in the same way once deployed via `semantic-release`, just replace `module-starter.leon` with the name of the module specified in `setup.py`.

## Development
In order to utilize the structure of this project for downstream modules, you should consider the following notes.

### Configuraiton
All module metadata lives within `setup.py`. This is where you link depenencies, specify source directories, and other important package metadata. A snippet of our `setup.py`:
```python

```