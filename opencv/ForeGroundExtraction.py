import numpy as np
import cv2
import matplotlib.pyplot as plt
img= cv2.imread('pihu.jpg')
##w=img.shape[0]
##h=img.shape[1]
##print(w,h)

mask=np.zeros(img.shape[:2],np.uint8)

bgdmodel = np.zeros((1,65),np.float64)
fgdmodel = np.zeros((1,65),np.float64)
rect=(100,79,400,250)
cv2.grabCut(img,mask,rect,bgdmodel,fgdmodel,5,cv2.GC_INIT_WITH_RECT)
mask2=np.where((mask==2)|(mask==0),0,1).astype('uint8')
img=img*mask2[:,:,np.newaxis]
plt.imshow(img)
plt.colorbar()
plt.show()
