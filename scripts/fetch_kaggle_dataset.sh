#!/usr/bin/env bash

BASE_DIR=$(pwd)
echo "Checking directory $(BASE_DIR)"

kaggle competitions download -c house-prices-advanced-regression-techniques -p /packages/regression_model/regression_model/datasets/
#unzip /home/circleci/project/packages/regression_model/regression_model/datasets/house-prices-advanced-regression-techniques.zip
dir