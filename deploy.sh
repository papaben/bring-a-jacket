#! /usr/bin/env sh
##
# The simplest deploy script ever
##

# So I can see what command failed
set -e

cd /usr/local/lib/dr-rain || exit 1

git fetch origin || exit 1
git reset --hard origin/master || exit 1