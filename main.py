import numpy as np
import cv2

canvas = np.zeros((600, 600, 3), dtype="uint8")


'''
zad1

canvas = np.zeros((600, 600, 3), dtype="uint8")
color = (255,0,0)
cv2.line(canvas,(300,300),(600,600),color,2)
cv2.imshow("canvas",canvas)
cv2.waitKey()
'''

'''
zad 2
canvas = np.zeros((400, 400, 3), dtype="uint8")
green = (0,255,0)
red= (0,0,255)
cv2.rectangle(canvas,(0,0),(100,50),green,2)
cv2.rectangle(canvas,(400,400),(100,100),red,2)
cv2.imshow("canvas",canvas)
cv2.waitKey()


'''
'''
zad3
canvas = np.zeros((300, 300, 3), dtype="uint8")
green = (0,255,0)
red= (0,0,255)
blue = (255,0,0)
cv2.circle(canvas,(40,40),40,blue)
cv2.circle(canvas,(150,150),60,red)
cv2.imshow("canvas",canvas)
cv2.waitKey()

'''
'''
zad4canvas = np.zeros((600, 600, 3), dtype="uint8")
green = (0,255,0)
red= (0,0,255)
blue = (255,0,0)
cv2.rectangle(canvas,(250,250),(350,350),green,2)
cv2.circle(canvas,(300,300),30,red)
cv2.imshow("canvas",canvas)
cv2.waitKey()



'''
'''
zad5
canvas = np.zeros((600, 600, 3), dtype="uint8")
green = (0,255,0)
red= (0,0,255)
blue = (255,0,0)
for r in range(0, 175, 10):
    cv2.rectangle(canvas, (300-r, 300-r), (300+r,300+r),green)
cv2.imshow("canvas",canvas)
cv2.waitKey()
'''
green = (0,255,0)
red= (0,0,255)
blue = (255,0,0)
img = cv2.imread("selfie.png")
h,w = img.shape[:2]
print(h)
print(w)
cv2.rectangle(img, (230,230), (390,420),green)
cv2.circle(img,(200,230),50,red)
cv2.circle(img,(360,230),50,red)
cv2.circle(img,(300,300),300,blue)



cv2.imshow("selfie",img)

cv2.waitKey()


