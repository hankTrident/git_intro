# -*- coding: utf-8 -*-
"""
Created on Thu May  7 17:57:30 2020

@author: HankWu
"""
from keras import models
from keras import layers
from keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np
from keras.utils import to_categorical

((train_images,train_labels),(test_images,test_labels))=mnist.load_data()
train_images.shape

network=models.Sequential()
network.add(layers.Dense(512,activation='relu',input_shape=(28*28,)))
network.add(layers.Dense(10,activation='softmax'))
network.compile(optimizer='rmsprop',loss='categorical_crossentropy',
                metrics=['accuracy'])

train_images=train_images.reshape((60000,28*28))
train_images=train_images.astype('float32')/255
test_images=test_images.reshape((10000,28*28))
test_images=test_images.astype('float32')/255
train_labels=to_categorical(train_labels)
test_labels=to_categorical(test_labels)

network.fit(train_images,train_labels,epochs=5,batch_size=128) #開始測

test_loss,test_acc=network.evaluate(test_images,test_labels)
print('test_acc:',test_acc)

x=train_images[500]
y=train_images[501]
z=train_images[502]
w=train_images[5]
pp=np.vstack((x,y))
pp1=np.vstack((z,w))
ppx=np.hstack((pp,pp1))

#plt.imshow(ppx,cmap='gray')
plt.imshow(ppx,cmap=plt.cm.binary)
plt.show()