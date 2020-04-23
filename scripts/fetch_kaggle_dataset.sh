#!/usr/bin/env bash

echo "==============Checking directory $(pwd)=================="
dir
kaggle competitions download -c house-prices-advanced-regression-techniques -p packages/regression_model/regression_model/datasets/


cd packages/regression_model/regression_model/datasets
echo "========cd to=======$(pwd)"
dir
echo "========after unziped======"
unzip house-prices-advanced-regression-techniques.zip
dir
