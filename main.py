import cv2
import numpy as np
from numpy.ma.core import bitwise_or

black = 0
white = 255

triangle = np.zeros((300, 300), dtype="uint8")
size = np.array([[[100, 50], [50, 150], [150, 150]]], dtype=np.int32)
cv2.fillPoly(triangle, size, color=white)

circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)

def zad1():
    cv2.imshow("or", cv2.bitwise_or(triangle, circle))
    cv2.imshow("and", cv2.bitwise_and(triangle, circle))
    cv2.imshow("nor", cv2.bitwise_xor(triangle, circle))
    cv2.imshow("xor", cv2.bitwise_not(triangle, circle))


    moved_circle = cv2.circle(circle, (40, 40), 20, 255, -1)
    cv2.imshow("moved", cv2.bitwise_or(triangle, moved_circle))
    cv2.waitKey(0)

def zad2():
    f1=cv2.imread("1.png")
    f2=cv2.imread("2.png")
    h,w = f1.shape[:2]
    f2_reseized = cv2.resize(f2,(w,h))
    cv2.imshow("compare",cv2.bitwise_xor(f1,f2_reseized))
    f1_gray = cv2.cvtColor(f1, cv2.COLOR_BGR2GRAY)
    f2_reseized_gray = cv2.cvtColor(f2_reseized, cv2.COLOR_BGR2GRAY)
    cv2.imshow("compare_gray",cv2.bitwise_xor(f1_gray,f2_reseized_gray))

    cv2.waitKey(0)



if __name__ == "__main__":
    zad2()