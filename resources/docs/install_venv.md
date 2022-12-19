# Venv installation script


## Install (pick one)
```bash
# sudo apt install python3.10-venv
pip install virtualenv
```

## Create venv (pick one)
```bash
# python3 -m venv venv  
virtualenv venv
# virtualenv venv --python=python3.7
```

## Activate venv (pick one)
```bash
venv\Scripts\activate 
# source venv/bin/activate
# source ./venv/Scripts/activate
# . venv/bin/activate # seems on windows was in scripts, and linux in binuname -a
# . venv/Scripts/activate
```

## Install in venv
```bash
# pip install package
# pip freeze > requirements.txt
# pip install -r requirements.txt
```

