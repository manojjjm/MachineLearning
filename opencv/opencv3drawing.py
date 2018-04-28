import numpy as np
import cv2
img= cv2.imread('watch.jpg',cv2.IMREAD_COLOR)
cv2.line(img,(0,0),(150,150),(255,255,255),15)

cv2.rectangle(img,(0,0),(45,60),(0,255,0),5)
cv2.circle(img,(100,63),55,(0,0,255),2)

##pts=np.array([[10,5],[15,20],[20,20],[15,20],[10,5]], np.int32)
###pts=pts.reshape(-1,1,2)
##cv2.polylines(img,[pts],True,(0,255,255),3)
##
##
##font=cv2.FONT_HERSHEY_SIMPLEX
##cv2.putText(img,'OPenCV TUTS',(0,15),font,1,(200,255,0),2,cv2.LINE_AA)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
