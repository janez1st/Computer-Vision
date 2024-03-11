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


# In[5]:


IMAGE_PATH = '/content/Liverpool.jpg'


# #Print All Text

# In[6]:


reader = easyocr.Reader(['en'])
result = reader.readtext(IMAGE_PATH)
result


# In[8]:


result[0]


# In[9]:


result[0][0]


# In[10]:


result[0][1]


# In[11]:


result[0][2]


# In[12]:


len(result)


# In[13]:


for i in range(len(result)-1):
  print(result[i][1])


# #Showing Picture

# In[7]:


img = cv2.imread(IMAGE_PATH)
plt.imshow(img)
plt.show()


# # Text Marking

# In[14]:


#Koordinat
result[0][0]


# In[15]:


#Pojok kiri atas dan kanan bawah
top_left = tuple(result[0][0][0])
bottom_right = tuple(result[0][0][2])
print(top_left)


# In[17]:


text = result[0][1]
text


# In[18]:


img = cv2.imread(IMAGE_PATH)
img = cv2.rectangle(img,top_left,bottom_right,(255,0,0),3)
plt.imshow(img)
plt.show()


# # All Text Marking

# In[19]:


img = cv2.imread(IMAGE_PATH)

for i in range(len(result)-1):
  top_left = tuple(result[i][0][0])
  bottom_right = tuple(result[i][0][2])
  img = cv2.rectangle(img,top_left,bottom_right,(255,0,0),3)


# In[20]:


plt.imshow(img)
plt.show()


# In[ ]:




