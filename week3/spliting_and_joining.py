#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import hashlib
from PIL import Image

from IPython.display import display

# # Load Image

# In[2]:


im_path = "baboon.png"

image = cv2.imread(im_path)

#display(Image.fromarray(image))


# In[3]:


image.shape


# # Split Image into Parts

# In[4]:


import matplotlib.pyplot as plt
import numpy as np
def split_image_into_parts(image, cols=5, rows=2):
    #img = cv2.imread('baboon.png')
 
    # cv2.imread() -> takes an image as an input

    img = cv2.imread('baboon.png')

    height, width ,channels = img.shape
    img_height = int(np.ceil(height / rows))
    img_width = int(np.ceil(width / cols))

    n_img = []
    for row in range(rows):
        for col in range(cols):
            x = col * img_width
            y = row * img_height
            sub_img = img[y:y+img_height, x:x+img_width]
            n_img.append(sub_img)
    #cv2.imshow('Top', top)
    #cv2.imshow('Bottom', bottom)# your code here
    return n_img



im_parts = split_image_into_parts(image, cols=11, rows=11)

# display parts
for img in im_parts:
    display(Image.fromarray(np.array(img)))
# your code here


# In[15]:


len(im_parts)


# In[13]:


rows,cols =11,11
height, width ,channels = img.shape
img_height = height // rows
img_width = width // cols
img = image
img_rws =[]
for row in range(rows):
    n_img = []
    for col in range(cols):
        x = cols * img_width
        y = rows * img_height
        sub_img = img[y:y+img_height, x:x+img_width]
        n_img.append(sub_img)
    img_rws.append(cv2.hconcat(n_img))   
#cv2.imshow('Top', top)

joined_image=cv2.vconcat(img_rws)
#cv2.imshow('Bottom', bottom)# your code here


# In[14]:


joined_image.shape


# In[6]:


'''import matplotlib.pyplot as plt
import numpy as np
def split_image_into_parts(image, cols=3, rows=2):
    #img = cv2.imread('baboon.png')
 
    # cv2.imread() -> takes an image as an input

    img = cv2.imread('baboon.png')

    height, width ,channels = img.shape
    img_height = round(height / rows)
    img_width = round(width / cols)

    n_img = []
    for row in range(rows):
        for col in range(cols):
            x = col * img_width
            y = row * img_height
            sub_img = img[y:y+img_height, x:x+img_width]
            n_img.append(sub_img)
    #cv2.imshow('Top', top)
    #cv2.imshow('Bottom', bottom)# your code here
    return n_img



im_parts = split_image_into_parts(image, cols=5, rows=5)

# display parts
for img in im_parts:
    display(Image.fromarray(np.array(img)))
# your code here
'''


# # Joining Back of Parts

# In[39]:



'''def join_image_parts(outer_list_tiles):
    x=cv2.hconcat(outer_list_tiles[0:len(outer_list_tiles)//])# your code here
    y= cv2.hconcat(outer_list_tiles[len(outer_list_tiles)//11:len(outer_list_tiles)])
    return cv2.vconcat([x,y])'''

#joined_image = join_image_parts(im_parts)
#joined_image = cv2.cvtColor(joined_image, cv2.COLOR_BGR2RGB)

#display(Image.fromarray(joined_image))


# In[47]:


rows=11
x=[]
def join_image_parts(outer_list_tiles):
    for i in range(len(outer_list_tiles)):
        horizontal_concat= cv2cv2.hconcat(outer_list_tiles[i:rows+i])
        x.append(horizontal_concat)
        i+=rows
    #x=[cv2.hconcat(row_list) for row_list in outer_list_tiles]# your code here
    #y= cv2.hconcat(outer_list_tiles[int(np.ceil(len(outer_list_tiles)/rows)):22])
    return x

joined_image = join_image_parts(np.array(im_parts))
joined_image = cv2.cvtColor(joined_image, cv2.COLOR_BGR2RGB)

display(Image.fromarray(joined_image))


# In[46]:


cv2.hconcat(im_parts[0:rows])


# In[35]:


[cv2.hconcat(row_list) for row_list in im_parts]


# In[20]:


int(np.ceil(len(im_parts)/rows))


# In[23]:


joined_image.shape


# # Save joined Image
# 

# In[ ]:


# your code here
cv2.imwrite("new_image.png",joined_image)


# # Compare Original and Saved Image Hashes (should be same)

# In[ ]:


def get_hash(file_path):
    return hashlib.md5(cv2.imread(file_path).tobytes()).hexdigest()

# Compare Hashes
new_im_path="new_image.png"
print("Hash of original Image:",get_hash(im_path))
print("Hash of New Image:",get_hash(new_im_path))


# In[ ]:


#Who has done splitting and joining but getting different hashes, can debug it by printing the hashes of loaded images too. In this was you can know if the hash issue occur due to joining or saving. You can use following code

import hashlib
def get_hash(file_path):
    return hashlib.md5(cv2.imread(file_path).tobytes()).hexdigest()

# Compare Hashes
print("Hash of original Loaded Image:",hashlib.md5(image.tobytes()).hexdigest())
print("Hash of Joined Loaded Image:",hashlib.md5(joined_image.tobytes()).hexdigest())
print()
print("Hash of original Saved Image:",get_hash(im_path))
print("Hash of New Saved Image:",get_hash(new_im_path))


# In[ ]:




