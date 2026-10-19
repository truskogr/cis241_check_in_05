#!/bin/bash

git branch gen
git switch gen

cp .secret/generate_story.py .
git add generate_story.py
git commit -m "Add generator"

cp .secret/madlibs.txt .
git add madlibs.txt
git commit -m "Add answers to madlibst.txt"

#git push origin gen

git switch main
