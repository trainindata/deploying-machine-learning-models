# Productionized Titanic Classification Model Package

## Get the data

- [Download](https://www.openml.org/data/get_csv/16826755/phpMYEkMl) the data from OpenML
- Save the downloaded file as `raw.csv` in the `titanic_model/datasets` directory


## Run With Tox (Recommended)

- Install tox (only when running for the first time)

    `pip install tox`

- In the `titanic-production` directory (where the tox.ini file is), run tox:

    `tox`
    
    This runs the tests and typechecks, trains the model under the hood.

    The first time you run this it creates a virtual env and installs dependencies, so it takes a few minutes.

    The trained model will be saved in `titanic_model/trained_models`


## Run Without Tox
- Add `titanic-production` *and* `titanic_model` paths to your system PYTHONPATH
- Install dependencies through requirements:

    `pip install -r requirements/test_requirements`

- Train the model:

    `python titanic_model/train_pipeline.py`

    The trained model will be saved in `titanic_model/trained_models`

- Run the tests

    `pytest tests`

