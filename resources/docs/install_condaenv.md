# Install an environment using Conda env

## Conda env installation 
___

```bash
export CONDA_ENV_NAME="streamlit_env"
echo "lets create a conda env : "$CONDA_ENV_NAME
```

## Create the environment
```bash
conda create -n $CONDA_ENV_NAME python=3.7
eval "$(conda shell.bash hook)"
```

## Activate the environment
```bash
conda activate $CONDA_ENV_NAME
#source activate $CONDA_ENV_NAME
```

## Add libraries
```bash
pip install -r requirements.txt
#conda env update -f environment.yml
```