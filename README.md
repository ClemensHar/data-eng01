# data-eng01
Scripts and prototyping notebooks wrt data engineering. 

## Git instructions

- Cloning the repository for the first time, use

    ```
    git clone --recursive git@github.com:polytech-com/python-packages.git
    ```

- Already have the repository cloned and you want to pull all the contents
    ```
    git pull
    git submodule update --recursive --init
    ```


## Setup environment in git-repository

- Ensure that you are using **python >= 3.9** for development purposes on your local workspace.

- Initialize a python environment

    - Unix based systems
        ```
        python3 -m venv env
        . env/bin/activate
        pip install -U pip setuptools wheel 
        pip install -r ./requirements.txt
        ```

    - Windows based systems on CMD
        ```
        py -m venv .env
        env\Scripts\activate.bat
        pip install -U pip setuptools wheel
        pip install -r ./requirements.txt
        ```
    ---
    **NOTE**

    Always refresh the environment after adding changes to python-modules within **path/to/git/repository/src**

    ```
    cd /path/to/git/submodule
    pip install .
    ```
    OR
    
    Install the python package in development mode in the first place
    ```
    cd /path/to/git/submodule
    pip install -e .
    ```
    
    ---

You could use [pyenv](https://realpython.com/intro-to-pyenv/) or [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-python.html) to

- install multiple python-versions within local workspace and
- switch between different python-versions.