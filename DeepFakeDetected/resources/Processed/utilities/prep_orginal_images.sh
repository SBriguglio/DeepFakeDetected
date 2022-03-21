#!/bin/bash

in_path="/home/brigugls/repositories/University_Repos/CourseWork/8700Project_DeepFakeDetection/DeepFakeDetected/DeepFakeDetected/resources/VidTIMIT"
out_path="/home/brigugls/repositories/University_Repos/CourseWork/8700Project_DeepFakeDetection/DeepFakeDetected/DeepFakeDetected/resources/Processed/originals"

mkdir $out_path || echo "out_path exists!"

for DIR in */; do
  cd "$in_path/$DIR" || return
  for subDir in */; do
    cd "$in_path/$DIR/$subDir" || return
    for subsubDir in */; do
      cd "$in_path/$DIR/$subDir/$subsubDir" || return
      for FILE in *; do
        newname=$(echo "$DIR$subsubDir$FILE" | tr -d "/")
        cp "$FILE" $out_path/"$newname.png"
      done
    done
  done
done
