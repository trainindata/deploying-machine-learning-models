#!/usr/bin/env bash

kaggle datasets download -d vbookshelf/v2-plant-seedlings-dataset -p packages/neural_network_model/neural_network_model/datasets/ && unzip packages/neural_network_model/neural_network_model/datasets/v2-plant-seedlings-dataset.zip -d packages/neural_network_model/neural_network_model/datasets/v2-plant-seedlings-dataset
