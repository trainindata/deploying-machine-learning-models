#!/usr/bin/env bash

DB=house-prices-advanced-regression-techniques
DEST=/home/circleci/project/packages/regression_model/regression_model/datasets
kaggle competitions download -c $DB -p $DEST/ && unzip $DEST/$DB.zip -d $DEST/