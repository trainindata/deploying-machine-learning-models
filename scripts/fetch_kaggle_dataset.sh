#!/usr/bin/env bash

echo "Checking directory $(pwd)"

kaggle competitions download -c house-prices-advanced-regression-techniques -p /packages/regression_model/regression_model/datasets/
#unzip /home/circleci/project/packages/regression_model/regression_model/datasets/house-prices-advanced-regression-techniques.zip
dir