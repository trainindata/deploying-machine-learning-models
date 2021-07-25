#!/usr/bin/env bash

#kaggle competitions download -c house-prices-advanced-regression-techniques -p packages/regression_model/regression_model/datasets/

kaggle competitions download house-prices-advanced-regression-techniques -f test.csv -p packages/regression_model/regression_model/datasets/
 
kaggle competitions download house-prices-advanced-regression-techniques -f train.csv -p packages/regression_model/regression_model/datasets/