#!/bin/bash

# Building packages and uploading them to a Gemfury repository

GEMFURY_URL=$GEMFURY_PUSH_URL
echo "GEMFURY_URL: $GEMFURY_URL"

set -e
set -x  # Enable debugging mode

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
    echo "BASE_DIR is $BASE_DIR"  # Debug info
    echo "Current directory is $(pwd)"  # Debug info
    cd "$BASE_DIR/$DIR"
    
    [ ! -e $SETUP ] && warn "No $SETUP file, skipping" && return
    PACKAGE_NAME=$(python $SETUP --fullname)
    
    echo "Package name is $PACKAGE_NAME"  # Debug info
    python "$SETUP" sdist bdist_wheel || die "Building package $PACKAGE_NAME failed"
    
    echo "Listing files in dist/ directory:"  # Debug info
    ls dist  # Debug info
    
    for X in $(ls dist); do
        echo "Uploading $X to Gemfury"  # Debug info
        curl -F package=@"dist/$X" "$GEMFURY_URL" || die "Uploading package $PACKAGE_NAME failed on file dist/$X"
    done
}

if [ -n "$DIRS" ]; then
    for dir in $DIRS; do
        echo "Processing directory: $dir"  # Debug info
        build $dir
    done
else
    ls -d */ | while read dir; do
        echo "Processing directory: $dir"  # Debug info
        build $dir
    done
fi
