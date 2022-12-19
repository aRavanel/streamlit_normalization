# Pipenv installation script

## Prerequisite
```bash
pip install pipenv # Install pipenv if not already installed
export PIPENV_VENV_IN_PROJECT=1  # If we want the virtualenv folder to be in project folder
```

## Create an environment
```bash
#pipenv install # Install a default version of python
pipenv install --python 3.7 #Install a specific version of python
```

## Activate
```bash
pipenv shell #Activate the environment
```

## Install libraries
```bash
pip install <package> --dev
```

## Clean if needed
```bash
Deactivate
Pipenv --rm #Remove env if error
```