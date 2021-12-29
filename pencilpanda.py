#!/usr/bin/env python
# coding: utf-8

# # DATA SCIENCE INTERN AT LETSGROWMORE(LGMVIP)

# # Name: Akhila Reddy Vancha

# # Task3: Image To Pencil sketch (Beginner Level)

# In[1]:


get_ipython().system('pip3 install opencv-python')
import numpy as np


# In[4]:


import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[16]:


img = cv2.imread('panda.jpg')
plt.figure(figsize=(6,6))
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB),cmap='gray')
plt.title("Original Panda Image")
plt.show()


# In[17]:


# CREATING A NEW IMAGE BY CONVERTING THE ORIGINAL IMAGE TO GREYSCALE
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure(figsize=(6,6))
plt.imshow(gray_image,cmap='gray')
plt.title("Greyscale Image")
plt.show()


# In[19]:


#INVERTING IMAGE OF panda
invert_image = 255 - gray_image
plt.figure(figsize=(6,6))
plt.imshow(invert_image,cmap='gray')
plt.title("Smoothen Image")
plt.show()


# In[20]:


#BLUR IMAGE BY USING THE GAUSSIAN FUNCTION
blurred = cv2.GaussianBlur(invert_image, (21, 21), 0)
plt.figure(figsize=(6,6))
plt.imshow(blurred,cmap='gray')
plt.title("Blurred Image")
plt.show()


# In[29]:


inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)


# In[27]:


plt.figure(figsize=(6,6))
plt.imshow(pencil_sketch,cmap='gray')
plt.title("Pencil sketch Image")
plt.show()


# In[ ]:




