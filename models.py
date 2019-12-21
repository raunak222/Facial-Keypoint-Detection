## TODO: define the convolutional neural network architecture

import torch
import torch.nn as nn
import torch.nn.functional as F
# can use the below import should you choose to initialize the weights of your Net
import torch.nn.init as I


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        
        ## TODO: Define all the layers of this CNN, the only requirements are:
        ## 1. This network takes in a square (same width and height), grayscale image as input
        ## 2. It ends with a linear layer that represents the keypoints
        ## it's suggested that you make this last layer output 136 values, 2 for each of the 68 keypoint (x, y) pairs
        
        # As an example, you've been given a convolutional layer, which you may (but don't have to) change:
        # 1 input image channel (grayscale), 32 output channels/feature maps, 5x5 square convolution kernel
         ## output size = (W-F)/S +1 = (224-5)/1 +1 = 220
        self.conv1 = nn.Conv2d(1, 32, 5)
        
        self.pool = nn.MaxPool2d(2, 2)
        ## output size = 220/2=110
        self.conv2 = nn.Conv2d(32, 64, 3)#output= 110-3/1 +1=108
        self.pool = nn.MaxPool2d(2, 2)#output=108/2=54
        ## Note that among the layers to add, consider including:
        self.conv3=nn.Conv2d(64,128,3)#output (54-3)/1+1=52
        self.pool = nn.MaxPool2d(2, 2) #output=52/2=26
        
        
        self.fc1 = nn.Linear(26*26*128,256)
      
        self.fc2 = nn.Linear(256,136)
       
        self.dropout=nn.Dropout(0.3)
        
    def forward(self, x):
        ## TODO: Define the feedforward behavior of this model
        ## x is the input image and, as an example, here you may choose to include a pool/conv step:
        ## x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv1(x)))
      
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))
        # prep for linear layer
        # this line of code is the equivalent of Flatten in Keras
        x = x.view(x.size(0), -1)
        x = self.dropout(x)
        # two linear layers with dropout in between
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        
        
        # a modified x, having gone through all the layers of your model, should be returned
        return x
