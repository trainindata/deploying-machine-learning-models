# Deploying Machine Learning Models
For the documentation, visit the course on Udemy.

diff from https://github.com/trainindata/deploying-machine-learning-models commit Section 8.4 - Publishing the model in CI

- in .circleci/config.yml

pip install -r packages/ml_api/requirements.txt

=>

pip install -r packages/ml_api/requirements.txt --trusted-host pypi.fury.io

- in scripts/fetch_kaggle_dataset.sh

kaggle competitions download -c house-prices-advanced-regression-techniques -p packages/regression_model/regression_model/datasets/

=>

kaggle competitions download house-prices-advanced-regression-techniques -f test.csv -p packages/regression_model/regression_model/datasets/

kaggle competitions download house-prices-advanced-regression-techniques -f train.csv -p packages/regression_model/regression_model/datasets/
