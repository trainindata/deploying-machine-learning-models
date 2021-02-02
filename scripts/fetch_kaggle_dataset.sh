#!/usr/bin/env bash

kaggle competitions download -c titanic -f test.csv -p packages/regression_model/regression_model/datasets/
 
kaggle competitions download -c titanic -f train.csv -p packages/regression_model/regression_model/datasets/