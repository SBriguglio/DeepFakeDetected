# Image Processing Utilities
Included in this folder are shell scripts to process images from the DeepfakeTIMIT 
and VidTIMIT datasets for use in model training. The scripts use ffmpeg to split the
DeepfakeTIMIT videos into frames at a native rate of 25 fps. This results in a dataset
of deepfake images roughly equivalent in size to the dataset of original frames provided
by the VidTIMIT dataset.

Care should be taken to review the shell scripts and modify them as needed, depending on
where your dataset files are located on your system.

The ```cropface.py``` utility will crop all image files in the ```../Processed/deepfake```
and ```../Processed/originals``` directories. It will output these files to the ```.../Processed/cropped```
directory in two separate folders. You should review this code to ensure it works with your
environment. You can expect processing times of about 900-1200 images/minute.

## IMPORTANT NOTE
You will need to remove the audio files from the VidTIMIT dataset for the ```prep_original_images.sh```
script to work properly. The shell scripts were also placed appropriately within the 
dataset folders. **They will not work from this directory**. Additionally, we only used the folders from the VidTIMIT dataset
which were used by the authors of the DeepfakeTIMIT dataset:
- fadg0
- faks0
- fcft0
- fcmh0
- fdac1
- fdrd1
- fedw0
- felc0
- fjas0
- fjem0
- fjre0
- fjwb0
- fkms0
- fram1
- mccs0
- mcem0
- mdab0
- mdbb0
- mdld0
- mdwt0
- mjar0
- mjsw0
- mmdb1
- mmdm2
- mpdf0
- mpgl0
- mrcz0
- mrgg0
- mrjo0
- msjs1
- mstk0
- mwbt0