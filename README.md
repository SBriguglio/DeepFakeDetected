# COMP 8700: Project Proposal

## Deepfake Detection Tool

### Ibraheem Aloran

### Spencer Briguglio

## Overview

Deepfakes are a relatively modern technology that has gained a lot of negative attention in recent years. Even though they can be fun or interesting images to share with others, they also have more sinister applications. Deepfake images and videos can be used to damage someone’s public image. It is well known that several high-profile public figures have had explicit photos generated using their likeness. It is not difficult to imagine that someone could use these images to blackmail or extort anyone who would not want the images to make it to the public eye. What is more worrying are the prospects of doctoring videos of political figures which represent entire nations to spread misinformation, steering elections, incite violence or declare war on neighboring countries. This is especially concerning during periods of tense political strife between nations like that which is currently ongoing between Russia and Ukraine who are fearful of a Russian invasion. If people cannot distinguish real photos and video from fabricated images, then some sort of deepfake detection tool should be available to help avoid these situations. 

We propose a deepfake detection tool that can accurately classify deepfake images and authentic photographs so that anyone can use this tool to help them distinguish between information and misinformation. Additionally, the machine learning model could also be used by web crawlers to detect fake media and record it to be removed or acted upon. This tool could be especially useful for anyone who commonly finds themselves in the public eye, but also for individuals who may be the victim of online abuse. It could also help journalists; law enforcement and other government entities verify information and protect people in an increasingly dangerous online environment. 

We aim to deliver an easy-to-use tool with a graphical user interface designed for the general computer user to interact with. To accomplish this goal, we will start by producing an artificial intelligence model that can accurately classify deepfake images. With video preprocessing, we will also expand the model to work with video input. Because we want to ensure a smooth user experience, we will also provide easy to understand instructions of how to import images and test them using our model. Additionally, we will include a disclaimer that no matter how accurate the model may be, it will never be completely accurate. We want to be transparent with our users so that they understand that results should not be assumed to be correct. 

Our production workflow will proceed as follows. Within the first two weeks of the commencing the project, we will have identified and become familiar with the most commonly used techniques to detect deepfakes (see literature review for more information). By mid-March, we will have created our own model and also have a way to deal with video files, likely by splitting them into separate image files. For the remainder of March, we will continue modifying the hyperparameters of the model to optimize it for our tool. We will begin GUI development shortly afterward. In the event that we are ahead of schedule, we have added some additional development milestones to our schedule. We would like to investigate labelling features in images that were responsible for a particular classification. This would be helpful for the user to make a proper assessment of the image using our tool’s results. Furthermore, we would also like to explore using GANs to generate more images with which to train our deepfake detection tool. Lastly, we would like to know if our tool could also be used to detect doctored but not entirely faked images. We suspect that because deepfakes are not always entire doctors, that the model may be able to detect image alterations in general. 

### Literature Review

In 2016, Malik et al. (Malik et al., 2022) conducted a thorough survey of the various tools for creating deepfakes and the uses of deepfakes. Among them, several malicious uses for deepfakes stand out. Identity swap, also known as face-swap, as its name suggests, is the process of swapping one face in an image with another from some other source. This can be used to create convincing videos of people which never happened. Attribute manipulation is also common and can be used to modify the expressions, facial features, hair color and other qualities of the person in the image. Face morphing is another technique which creates an artificial biometric face sample that mimics the biometric data of multiple people. This type of manipulation can lead to significant security breaches as it has been shown to be able to trick facial recognition systems into falsely verifying identities, clearly necessitating the need for accurate and robust deepfake identification tools. 

There are several ways to distinguish Deepfake videos and pictures. Guera et al. (Guera & Delp, 2019) explored the weaknesses of deepfake generation and found that intra-frame inconsistencies and temporal inconsistencies are created when generating deepfakes. They exploited them using two sets of autoencoder-decoders with shared weights. They also found that in generating the final video the autoencoder is used frame by frame, so it is not aware of any face or image it has previously created. Exposing these anomalies helped in identifying deepfakes. They used a CNN for frame feature extraction and LSTM for temporal sequence analysis. Al-Dhabi et al. (Al-Dhabi & Zhang, 2021) proposed a method for detection based on the same method used for generating deepfake videos. They combined convolutional neural network (CNN) with recurrent neural network (RNN) to try and achieve better results and a higher accuracy.  

Most deepfake detection methods are generally based on the techniques used to create them, such as Generative Adversarial Networks (GANs). Guarnera et al. (Guarnera et al., 2020) proposed a different approach than the usual ones. They attempted to capture traces of deepfakes by reverse engineering the last layer of a given GAN. They extracted and analyzed the convolutional traces generated by the GANs. This will give more explainability to the predictions and will be of great use to forensic investigations. They claim that their method will be able to classify deepfake images and videos and predict the most probable technique used to generate it. 

Zhang et al. (Zhang, 2022) and Nguyen et al. (Nguyen et al., 2019) also report on many other state-of-the-art methods for deepfake creation and detection. Of the papers surveyed, CNNs appear to be the most widely used method of detection. Many of them are designed to detect specific features in the images, but many leverage the feature extraction ability of CNNs to extract and map features to a correct classification. These methods have exceptionally high accuracy (highest reported accuracy of 0.9993 by Zhao et al. (Zhao et al., 2020)). Other methods include deep neural networks (DNNs), state vector machines (SVMs) and other neural network architectures. More recently, Jeong et al. proposed FrePGAN, (Jeong et al., 2022) a robust deepfake detection framework which displayed state-of-the-art performance. The framework uses GANs to generate increasingly difficult examples to train a classifier and was able to detect deepfakes better than many other state-of-the-art methods. Interestingly, they were able to show state-of-the-art performance even with images which don’t fall into categories commonly associated with deepfakes. For example, an image of a horse being groomed by its rider. It could be that these types of models become increasingly important in the future as image generation expands into generating other scenes beside human portraits which opens an entirely new realm of possible malign uses. Clearly, deepfake detection will need to become much more robust and applicable to a wide range of use cases.  

## Project Goal

We aim to develop a model/tool that will allow users to classify deepfakes and verify the authenticity of photos. The model will be able to detect fake images and videos similar to the dataset used to train it. We hope to create a tool from this machine learning model that a user will be able to interact with using a simple graphical user interface. The tools development will be constrained to image/video detection only and may only be able to process images/videos of a certain format. 

## Project Team

| Name              | Description                                                  |
| ----------------- | ------------------------------------------------------------ |
| Ibraheem Aloran   | Experience with python, C and Java. Researching federated learning with blockchain |
| Spencer Briguglio | Researching federated learning and cybersecurity, most comfortable with Python and C++, some experience with OpenCV and Qt5 |

## Schedule and Milestones

| Milestone                                | Description                                                  | Milestone Criteria                                           | Planned Date     |
| ---------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------------- |
| Begin Project                            | To begin development of the project, we need to develop our understanding of the problem and what tools might be relevant to producing our solution | \- framework, library, dataset and language selected and understood enough to use <br />\- identify possible ML models to use | March 4th, 2022  |
| Basic Detection Model                    | The largest risk to the project is not having a model which is capable of classifying images as deepfakes or authentic images. Further, we need to have a method to preprocess data so that it can be used to train the model. If model training is highly resource intensive, we may need to be prepared to use cloud computing or other ML computation solutions. | - first ML model(s) implemented<br />- preprocess data<br />- other preparation for training | March 18th, 2022 |
| Model Training and Hyperparameter Tuning | With a tested and functional model, we will focus on optimization so that our deepfake detection tool is as accurate as possible for users. | -maximize model accuracy                                     | April 1st, 2022  |
| UI Development and Report                | Most users are not familiar enough with command line interfaces to use a tool like this. Therefore, we will aim to create a simple yet effective graphical user interface that is easy to use. To address ethical concerns, we will also inform users that an image’s classification can never be 100% accurate and that these results should only be used to offer insight for their judgement. | - GUI created that allows users to test images with a trained model<br />- GUI allows user to train the model further and then test image<br /> - GUI displays image being classified and its classification<br />- final report completed | April 10th, 2022 |

## Communication and Reporting

We will hold standup meetings on Discord twice a week (Mondays at 10:00 am and Fridays at 3:00 pm) to discuss project development, risks, and issues, and plan next steps. Other meetings may be scheduled at the group member’s discretion. All reporting of information and communications will primarily be through Discord and/or the GitHub repository, https://github.com/SBriguglio/DeepFakeDetected. 

## Delivery Plan

**Deliverable I:** A basic ML model can accurately classify images from a test set created from open-source datasets used to train the model. (March 18th to project group) 

**Deliverable II:** The ML model can accurately classify generated or new images which are similar those used to train the model but NOT from the same datasets used to train the model. (April 1st to project group) 

**Deliverable III:** The ML model can accept image or video files and/or a tool has been developed to preprocess data before being used in model training. (April 1st to project group) 

**Deliverable IV:** The user can import a video or image file into the tool which will then be classified as fake or legitimate, with reasonably high accuracy. (April 10th to user) 

**Deliverable V:** The user can view the certainty that an imported/image is properly classified as fake or legitimate. (April 10th to user) 

**Deliverable VI:** The tool has clear instructions for the user to import and classify images. The tool clearly states which images/videos will obtain the best results as well as any constraints the tool has. (April 10th to user) 

## Bibliography

Al-Dhabi, Y., & Zhang, S. (2021). Deepfake Video Detection by Combining Convolutional Neural Network (CNN) and Recurrent Neural Network (RNN). *2021 IEEE International Conference on Computer Science, Artificial Intelligence and Electronic Engineering, CSAIEE 2021*, 236–241. https://doi.org/10.1109/CSAIEE54046.2021.9543264 

Guarnera, L., Giudice, O., & Battiato, S. (2020). DeepFake detection by analyzing convolutional traces. *IEEE Computer Society Conference on Computer Vision and Pattern Recognition Workshops*, *2020-June*, 2841–2850. https://doi.org/10.1109/CVPRW50498.2020.00341 

Guera, D., & Delp, E. J. (2019). Deepfake Video Detection Using Recurrent Neural Networks. *Proceedings of AVSS 2018 - 2018 15th IEEE International Conference on Advanced Video and Signal-Based Surveillance*. https://doi.org/10.1109/AVSS.2018.8639163 

Jeong, Y., Kim, D., Ro, Y., & Choi, J. (2022). *FrePGAN: Robust Deepfake Detection Using Frequency-level Perturbations*. http://arxiv.org/abs/2202.03347 

Malik, A., Kuribayashi, M., Abdullahi, S. M., & Khan, A. N. (2022). DeepFake Detection for Human Face Images and Videos: A Survey. *IEEE Access*, *PP*, 1–1. https://doi.org/10.1109/access.2022.3151186 

Nguyen, T. T., Nguyen, Q. V. H., Nguyen, D. T., Nguyen, D. T., Huynh-The, T., Nahavandi, S., Nguyen, T. T., Pham, Q.-V., & Nguyen, C. M. (2019). *Deep Learning for Deepfakes Creation and Detection: A Survey*. https://doi.org/10.2139/ssrn.4030341 

Zhang, T. (2022). Deepfake generation and detection, a survey. *Multimedia Tools and Applications*, *August 2020*. https://doi.org/10.1007/s11042-021-11733-y 

Zhao, Z., Wang, P., & Lu, W. (2020). Detecting Deepfake Video by Learning Two-Level Features with Two-Stream Convolutional Neural Network. *ACM International Conference Proceeding Series*, 291–297. https://doi.org/10.1145/3404555.3404564 