#!/bin/bash
# A shell script file to process videos into images for model training

in_path="/home/brigugls/repositories/University_Repos/CourseWork/8700Project_DeepFakeDetection/DeepfakeTIMIT/DeepfakeTIMIT/lower_quality/"
out_path="/home/brigugls/repositories/University_Repos/CourseWork/8700Project_DeepFakeDetection/DeepFakeDetected/DeepFakeDetected/resources/Processed/deepfakes"

mkdir $out_path || echo "out_path exists!"

cd $in_path || return

for DIR in */; do
  cd "$in_path/$DIR" || break;
  for FILE in *.avi; do
    [ -f "$FILE" ] || break;
    filename=$(echo "$FILE" | cut -f 1 -d '.');
    newname=$(echo "$DIR$filename" | tr -d "/");
    ffmpeg -i "$FILE" -r 25 -f image2 $out_path/"$newname"%07d.jpg;
  done
done

