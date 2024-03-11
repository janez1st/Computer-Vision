#!/usr/bin/env python
# coding: utf-8

# # Optical Character Recognition with EasyOCR

# In[ ]:


pip install easyocr


# In[4]:


import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np


IMAGE_PATH = '/content/Liverpool.jpg'


# #Print All Text

reader = easyocr.Reader(['en'])
result = reader.readtext(IMAGE_PATH)
result


result[0]

result[0][0]

result[0][1]

result[0][2]

In[12]:

len(result)

for i in range(len(result)-1):
  print(result[i][1])


# #Showing Picture

img = cv2.imread(IMAGE_PATH)
plt.imshow(img)
plt.show()


# # Text Marking

#Koordinat
result[0][0]


#Pojok kiri atas dan kanan bawah
top_left = tuple(result[0][0][0])
bottom_right = tuple(result[0][0][2])
print(top_left)


text = result[0][1]
text

img = cv2.imread(IMAGE_PATH)
img = cv2.rectangle(img,top_left,bottom_right,(255,0,0),3)
plt.imshow(img)
plt.show()


# # All Text Marking

img = cv2.imread(IMAGE_PATH)

for i in range(len(result)-1):
  top_left = tuple(result[i][0][0])
  bottom_right = tuple(result[i][0][2])
  img = cv2.rectangle(img,top_left,bottom_right,(255,0,0),3)

plt.imshow(img)
plt.show()
