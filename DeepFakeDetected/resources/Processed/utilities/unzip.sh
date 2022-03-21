#!/bin/bash

for DIR in */; do
  echo "$DIR"
  #cd "$DIR" || break
  rm -r "$DIR/audio"
done