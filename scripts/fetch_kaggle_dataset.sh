#!/usr/bin/env bash

kaggle competitions download -c house-prices-advanced-regression-techniques -p packages/regression_model/regression_model/datasets/
unzip packages/regression_model/regression_model/datasets/house-prices-advanced-regression-techniques.zip -d packages/regression_model/regression_model/datasets/