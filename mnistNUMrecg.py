#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt # This is all you need to import keras.datasets.mnist.load_data()


# In[2]:


# these imports are for afer cell 92
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization


# In[3]:


pixel_width = 28
pixel_height = 28
batch_size = 32
num_of_classes = 10
epochs=10


# In[4]:


(features_train, labels_train), (features_test, labels_test) = keras.datasets.mnist.load_data()
print(features_train.shape)


# In[5]:


features_train = features_train.reshape(features_train.shape[0],pixel_width,pixel_height,1)
print(features_train.shape)

features_test = features_test.reshape(features_test.shape[0],pixel_width,pixel_height,1)
print(features_test.shape)


# In[9]:


input_shape = (pixel_width, pixel_height,1)


# In[13]:


features_train =features_train.astype('float32')
features_test =features_test.astype('float32')


# In[15]:


features_train /=255
features_test /=255


# In[17]:


print(labels_train[5])


# In[19]:


# flatten 2 into a binary class matrix
labels_train=keras.utils.to_categorical(labels_train, num_of_classes)
labels_test=keras.utils.to_categorical(labels_test,num_of_classes)


# In[26]:


print(labels_train[5])


# In[32]:


# Caleb Stultz way, the model gets 88-90% @ 10 epochs

model = Sequential()
model.add(Conv2D(32, kernel_size=(3,3),activation='relu',input_shape=input_shape))
#print('POST CONV2D:', model.output_shape)
model.add(MaxPooling2D(pool_size=(2,2)))
#print('POST MAXPOOLING2D:', model.output_shape)
model.add(Dropout(0.25))
#print('POST DROPOUT:', model.output_shape)
model.add(Flatten())
#print('POST FLATTEN:', model.output_shape)
model.add(Dense(128,activation='relu'))
#print('POST DENSE:', model.output_shape)
model.add(Dense(num_of_classes,activation='softmax'))
#print('POST SOFTMAX:', model.output_shape)

model.compile(
    loss=keras.losses.CategoricalCrossentropy(),  # Correct loss function
    optimizer=keras.optimizers.Adadelta(), 
    metrics=['accuracy']
)


# In[ ]:


model.fit(features_train, labels_train,
          batch_size=batch_size,
          epochs=epochs, 
          verbose=1,
          validation_data=(features_test, labels_test))

score = model.evaluate(features_test, labels_test, verbose=0)


# In[34]:


print(score)


# In[ ]:




