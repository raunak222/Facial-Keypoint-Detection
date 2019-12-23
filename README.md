# Facial-Keypint-Detection
This is a repository of my project facial keypoints detection. This is the first project of my Computer Vision  Nanodegree
![alt text](https://github.com/raunak222/Facial-Keypint-Detection/blob/master/Images/key_pts_example.png)

## Introduction:
- Facial Key Points (FKPs) detection is an important and
challenging problem in the field of computer vision, which
involves detecting FKPs like centers and corners of eyes,
nose tip, etc. The problem is to predict the (x, y) realvalued co-ordinates in the space of image pixels of the FKPs
for a given face image. It finds its application in tracking
faces in images and videos, analysis of facial expressions,
detection of dysmorphic facial signs for medical diagnosis,
face recognition, etc.

##  Motivation/Purpose: 
- Main Purpose of this project is to detect facial keypoint from a given image dataset. So first we define the CNN Architecture for this 
### CNN Architecture
- Convolutional layers
- Maxpooling layers
- Fully-connected layers
in model.py file
Then We detect the face using Haar Cascade classifier after detecting frontial faces we pass these detected faces to trained model

##  How to Use 
- Go through instruction [here](https://github.com/raunak222/Facial-Keypint-Detection/blob/master/Instruction.txt)

##  Some Visualization
 ![alt text](https://github.com/raunak222/Facial-Keypint-Detection/blob/master/Images/haar_cascade_ex.png)
## Input Image
![alt text](https://github.com/raunak222/Facial-Keypint-Detection/blob/master/Images/download%20(3).png)
### Output Image
![alt text](https://github.com/raunak222/Facial-Keypint-Detection/blob/master/Images/detect.png)
### Output Image
![alt text](https://github.com/raunak222/Facial-Keypint-Detection/blob/master/Images/download%20(1).png)
## Using CNN Model
![alt text](https://github.com/raunak222/Facial-Keypint-Detection/blob/master/Images/screen-shot-2018-05-31-at-3.43.06-pm.png)
## We will  

- Change the number of convolutional layers and see what happens.
- Increase the size of convolutional kernels for larger images.
- Change loss/optimization functions to see how our model responds. 
- Add layers to prevent overfitting.
- Change the batch_size of your data loader to see how larger batch sizes can affect our training.
.
## Developer 
  Raunak Sarada  
  - [Github](https://github.com/raunak222) 
  - [linkedin](https://www.linkedin.com/in/raunak-sarada)
## Resources 
- https://github.com/udacity/P1_Facial_Keypoints
- https://blog.openmined.org
- https://arxiv.org/pdf/1710.00977.pdf

## Citation
- Udacity Computer Vision Nanodegree
