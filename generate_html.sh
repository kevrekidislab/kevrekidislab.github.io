#!/bin/bash
set -e
HERE=$(dirname "$0")
cd "$HERE"

mkdir -p notebooks_html

cd notebooks
IFS='
'
for notebook in $(ls *.ipynb)
do
    echo "Found notebook: \"$notebook\"."
    jupyter nbconvert "$notebook" --to html --output-dir="$HERE/notebooks_html"
done
