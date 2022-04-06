#!/bin/bash
# A shell script file to split processed files into training and validation data

in_DF_path="/home/brigugls/repositories/University_Repos/CourseWork/8700Project_DeepFakeDetection/DeepFakeDetected/DeepFakeDetected/DeepFakeDetected/resources/Processed/deepfakes/"
in_OR_path="/home/brigugls/repositories/University_Repos/CourseWork/8700Project_DeepFakeDetection/DeepFakeDetected/DeepFakeDetected/DeepFakeDetected/resources/Processed/originals/"
out_path="/home/brigugls/repositories/University_Repos/CourseWork/8700Project_DeepFakeDetection/DeepFakeDetected/DeepFakeDetected/DeepFakeDetected/resources/Processed/split/"
out_T_path="${out_path}train/"
out_V_path="${out_path}validate/"

mkdir $out_path || echo "out_path exists!"
mkdir "$out_T_path" || echo "training path exists!"
mkdir "$out_T_path/deepfakes/" || echo "training df path exists!"
mkdir "$out_T_path/originals/" || echo "training or path exists!"
mkdir "$out_V_path" || echo "validate path exists!"
mkdir "$out_V_path/deepfakes/" || echo "validate df path exists!"
mkdir "$out_V_path/originals/" || echo "validate or path exists!"

# Selected Files (Selecting 4 so that we have equal distribution of males and females)
str1="fadg0"
str2="fjwb0"
str3="mjsw0"
str4="mpg10"

declare -i v_count=0
declare -i t_count=0

# Split Deepfakes
df_count=0
cd $in_DF_path || return
echo "Splitting Deepfakes..."
for DF_FILE in *.jpg; do
  [ -f "$DF_FILE" ] || break;
  if [[ "$DF_FILE" == "$str1"* ]]; then
    cp "$DF_FILE" "$out_V_path/deepfakes/$DF_FILE"
    ((v_count+=1))
  elif [[ "$DF_FILE" == "$str2"* ]]; then
    cp "$DF_FILE" "$out_V_path/deepfakes/$DF_FILE"
    ((v_count+=1))
  elif [[ "$DF_FILE" == "$str3"* ]]; then
    cp "$DF_FILE" "$out_V_path/deepfakes/$DF_FILE"
    ((v_count+=1))
  elif [[ "$DF_FILE" == "$str4"* ]]; then
    cp "$DF_FILE" "$out_V_path/deepfakes/$DF_FILE"
    ((v_count+=1))
  else
    cp "$DF_FILE" "$out_T_path/deepfakes/$DF_FILE"
    ((t_count+=1))
  fi
  ((df_count+=1))
done

# Split Originals
or_count=0
cd $in_OR_path || return
echo "Splitting Originals..."
for OR_FILE in *.jpg; do
  [ -f "$OR_FILE" ] || break;
  if [[ "$OR_FILE" == "$str1"* ]]; then
    cp "$OR_FILE" "$out_V_path/originals/$OR_FILE"
    ((v_count+=1))
  elif [[ "$OR_FILE" == "$str2"* ]]; then
    cp "$OR_FILE" "$out_V_path/originals/$OR_FILE"
    ((v_count+=1))
  elif [[ "$DF_FILE" == "$str3"* ]]; then
    cp "$OR_FILE" "$out_V_path/originals/$OR_FILE"
    ((v_count+=1))
  elif [[ "$DF_FILE" == "$str4"* ]]; then
    cp "$OR_FILE" "$out_V_path/originals/$OR_FILE"
    ((v_count+=1))
  else
    cp "$OR_FILE" "$out_T_path/originals/$OR_FILE"
    ((t_count+=1))
  fi
  ((or_count+=1))
done

echo "Split Complete"
echo "DF Files = $df_count"
echo "OR Files = $or_count"
echo "Train Files = $t_count"
echo "Validation Files = $v_count"

((total=(t_count+v_count)))

printf "Actual Validation Split: "
printf %.1f "$((10**1 * 100*v_count/total ))e-1"
echo "%"
echo ""