import os
import configparser
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

config = configparser.ConfigParser()
config.read("set.ini")
path = config['default']['receipts'] 
print(path)
img = cv.imread(path + '2020/03/test.jpg',0)

ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
cv.imwrite(os.path.join(path , 'test1.jpg'), thresh1)
cv.imwrite(os.path.join(path , 'test2.jpg'), thresh2)
cv.imwrite(os.path.join(path , 'test3.jpg'), thresh3)
cv.imwrite(os.path.join(path , 'test4.jpg'), thresh4)
cv.imwrite(os.path.join(path , 'test5.jpg'), thresh5)
plt.show()
