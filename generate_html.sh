#!/bin/bash
set -e
THIS=$(readlink -f "$0")
HERE=$(dirname "$THIS")
cd "$HERE"
HERE=$(pwd)  # Convert to absolute path.

mkdir -p notebooks_html

cd notebooks
IFS='
'

for notebook in $(ls *.ipynb)
do
    echo "Found notebook: \"$notebook\"."
    jupyter nbconvert "$notebook" --to html --output-dir="$HERE/notebooks_html"
done

cd "$HERE"
python templates/index.py > index.html
