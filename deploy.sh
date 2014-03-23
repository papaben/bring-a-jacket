#! /usr/bin/env sh
##
# The simplest deploy script ever
##

# Don't keep deploying if poop hits the fan
set -e
# So I can see what command failed
set -x

cd /usr/local/lib/dr-rain || exit 1

git fetch origin || exit 1
git reset --hard origin/master || exit 1
