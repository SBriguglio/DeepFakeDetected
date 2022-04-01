#!/bin/bash
DF_PATH="/home/brigugls/repositories/University_Repos/CourseWork/8700Project_DeepFakeDetection/DeepFakeDetected/DeepFakeDetected/DeepFakeDetected/resources/Processed/uncropped/deepfakes/"
OR_PATH="/home/brigugls/repositories/University_Repos/CourseWork/8700Project_DeepFakeDetection/DeepFakeDetected/DeepFakeDetected/DeepFakeDetected/resources/Processed/uncropped/originals/"

echo "Renaming deepfakes. Please wait..."
cd $DF_PATH || return
COUNT=0
for IMAGE in *.jpg; do
  [ -f "$IMAGE" ] || break;
  N=$(printf '%06d' $COUNT);
  mv "$IMAGE" "deepfakes_image_${N}.jpg"
  COUNT=$((COUNT+1))
done
echo $COUNT

echo "Renaming originals. Please wait..."
cd $OR_PATH || return
COUNT=0
for IMAGE in *.jpg; do
  [ -f "$IMAGE" ] || break
  N=$(printf '%06d' $COUNT)
  mv "$IMAGE" "originals_image_${N}.jpg"
  COUNT=$((COUNT+1))
done
echo $COUNT

echo "Complete."