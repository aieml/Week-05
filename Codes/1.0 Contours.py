import cv2

img=cv2.imread('Materials/shapes.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray,50,255,cv2.THRESH_BINARY)

ret,contours,hierachy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

##cnt=contours[0]
##
##print(cnt.shape)
##print(cnt)

for cnt in contours:

    for val in cnt:

        (x,y)=val[0]
        cv2.circle(img,(x,y),5,(0,255,255),-1)

#cv2.drawContours(img,[cnt],0,(0,255,0),3)

cv2.imshow('IMG',img)
#cv2.imshow('GRAY',gray)
#cv2.imshow('THRESH',thresh)
