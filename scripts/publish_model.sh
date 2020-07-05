#!/bin/bash

# Building packages and uploading them to a Gemfury repository

GEMFURY_URL=$PIP_EXTRA_INDEX_URL

# Find the setup.py file
# We will run: ./scripts/publish_model.sh ./packages/regression_model/
# So we say that we should look for this file in ./packages/regression_model/

set -e

DIRS="$@"
BASE_DIR=$(pwd)
SETUP="setup.py"

warn() {
    echo "$@" 1>&2
}

die() {
    warn "$@"
    exit 1
}

build() {
    DIR="${1/%\//}"
    echo "Checking directory $DIR"
    cd "$BASE_DIR/$DIR"
    [ ! -e $SETUP ] && warn "No $SETUP file, skipping" && return
    PACKAGE_NAME=$(python $SETUP --fullname)
    echo "Package $PACKAGE_NAME"
    # We generate the distribution: the trained model
    python "$SETUP" sdist bdist_wheel || die "Building package $PACKAGE_NAME failed"
    # We loop over the distributed files
    for X in $(ls dist)
    do
        # We upload them to Gemfury
        curl -F package=@"dist/$X" "$GEMFURY_URL" || die "Uploading package $PACKAGE_NAME failed on file dist/$X"
    done
}

if [ -n "$DIRS" ]; then
    for dir in $DIRS; do
        build $dir
    done
else
    ls -d */ | while read dir; do
        build $dir
    done
fi