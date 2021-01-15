#!/usr/bin/env bash

TRAINING_DATA_URL="vbookshelf/v2-plant-seedlings-dataset"
NOW=$(date)

kaggle datasets download -d $TRAINING_DATA_URL -p packages/neural_network_model/neural_network_model/datasets/ && \
unzip packages/neural_network_model/neural_network_model/datasets/v2-plant-seedlings-dataset.zip -d packages/neural_network_model/neural_network_model/datasets/v2-plant-seedlings-dataset && \
echo $TRAINING_DATA_URL 'retrieved on:' $NOW > packages/neural_network_model/neural_network_model/datasets/training_data_reference.txt && \
mkdir -p "./packages/neural_network_model/neural_network_model/datasets/v2-plant-seedlings-dataset/Shepherds Purse"  && \
ls "./packages/neural_network_model/neural_network_model/datasets/v2-plant-seedlings-dataset/"  && \
FOLDER=(`ls ./packages/neural_network_model/neural_network_model/datasets/v2-plant-seedlings-dataset/`)
echo ${FOLDER[14]}
echo ${FOLDER[15]}
VAR1="./packages/neural_network_model/neural_network_model/datasets/v2-plant-seedlings-dataset/"
VAR2=${FOLDER[14]}
VAR3=${FOLDER[15]}
VAR4=" "
echo "$VAR1$VAR2$VAR4$VAR3"
#mv -v "./packages/neural_network_model/neural_network_model/datasets/v2-plant-seedlings-dataset/Shepherd's Purse/"* "./packages/neural_network_model/neural_network_model/datasets/v2-plant-seedlings-dataset/Shepherds Purse"
mv -v "$VAR1$VAR2$VAR4$VAR3"* "./packages/neural_network_model/neural_network_model/datasets/v2-plant-seedlings-dataset/Shepherds Purse"

#rm -rf "./packages/neural_network_model/neural_network_model/datasets/v2-plant-seedlings-dataset/Shepherd's Purse" 
rm -rf "$VAR1$VAR2$VAR4$VAR3"
