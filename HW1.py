#Libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt

#Additional Functions
def noisy(noise_typ,image):
   if noise_typ == "gauss":
      row,col,ch= image.shape
      mean = 0
      var = 0.1
      sigma = var**0.5
      gauss = np.random.normal(mean,sigma,(row,col,ch))
      gauss = gauss.reshape(row,col,ch)
      noisy = image + gauss
      return noisy
   elif noise_typ == "s&p":
      row,col,ch = image.shape
      s_vs_p = 0.5
      amount = 0.1
      out = np.copy(image)
      # Salt mode
      num_salt = np.ceil(amount * image.size * s_vs_p)
      coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in image.shape]
      out[coords] = 1

      # Pepper mode
      num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
      coords = [np.random.randint(0, i - 1, int(num_pepper))
              for i in image.shape]
      out[coords] = 0
      return out

#Reading image rgb and gray
img = cv2.imread('Robit.jpeg')
imggray=cv2.imread('Robit.jpeg',0)

#Making some effect and fixing process
blur = cv2.blur(img,(10,10))
imgsp=noisy("s&p",img)
imgblurplussp=noisy("s&p",blur)
gamma = np.array(255*(imggray/255)**2.0,dtype='uint8')
gamma_adj = np.array(255*(gamma/255)**0.5,dtype='uint8')

#Show all images.
cv2.imshow('img',img)
cv2.imshow('imggray',imggray)
cv2.imshow('blur',blur)
cv2.imshow('imgsp',imgsp)
cv2.imshow('imgblurplussp',imgblurplussp)
cv2.imshow('gamma',gamma)
cv2.imshow('gamma_adj',gamma_adj)

#To close all windows enter any key. If you close windows and terminal still processing use ctrl+z to close terminal process.
cv2.waitKey(0)
cv2.destroyAllWindows()