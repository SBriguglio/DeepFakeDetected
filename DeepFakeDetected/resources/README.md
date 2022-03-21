# Resource Files
## Datasets
The DeepfakeTIMIT<sup>1</sup> database of videos was used for this experiment along with
the VidTIMIT<sup>2</sup> dataset used as the training set for the original, unmodified 
videos. the DeepfakeTIMIT dataset was created using the VidTIMIT dataset and we hope that
our model can learn to identifiy the perturbations caused by deepfake generations by 
using both the deepfake and source material in image classification. You can find out
more information about the DeefakeTIMIT dataset [here](https://zenodo.org/record/4068245#.YjZwNjxE1o8)
and the VidTIMIT dataset [here](https://conradsanderson.id.au/vidtimit/#overview).
## Video-to-Image Processing
A shell script can be used to split videos into their subsequent frames for use in model
training. We hope to implement an algorithm which leverages the temporal nature of video
files in later contributions.

## References
1. P. Korshunov and S. Marcel, DeepFakes: a New Threat to Face Recognition? Assessment and Detection. [arXiv](https://arxiv.org/abs/1812.08685)
and [Idiap Research Report](http://publications.idiap.ch/index.php/publications/show/3988)
2. C. Sanderson and B.C. Lovell, Multi-Region Probabilistic Histograms for Robust and Scalable Identity Inference. , Lecture Notes in Computer Science (LNCS), Vol. 5558, pp. 199-208, 2009.