#!/bin/bash

set -x

git pull
git add *
git commit -am "$(date): $1"
git push
