from email.mime import image

import cv2


def zad1():
    img = cv2.imread('img.png')
    roi = img[0:100,0:100]
    cv2.imshow('img', roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def zad2():
    img = cv2.imread('img.png')
    h,w = img.shape[:2]
    roi = img[h//2:h,0:w]
    cv2.imshow('img', roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def zad3():
    img = cv2.imread('img.png')
    h,w = img.shape[:2]
    roi = img[0:h,w//2:w]
    cv2.imshow('img', roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def zad4():
    sX = input("sX")
    eX = input("eX")
    sY = input("sY")
    eY = input("eY")
    img = cv2.imread('img.png')
    roi = img[int(sY):int(eY),int(sX):int(eX)]
    cv2.imshow('img', roi)
    cv2.waitKey(5000)
def zad5():
    img = cv2.imread('img.png')
    h,w = img.shape[:2]
    roi = img[55:h-50,59:w-50]
    cv2.imshow('img', roi)
    cv2.waitKey(5000)
def zad6():
    img = cv2.imread('img.png')
    h,w = img.shape[:2]
    roi = img[0:100,0:100]
    img[h-100:h,w-100:w] = roi[0:100,0:100]
    cv2.imshow('img', img)
    cv2.waitKey(5000)
def zad7():
    img = cv2.imread('img.png')
    h,w = img.shape[:2]
    hh = h//9
    ww = w//9
    for i in range(0,8):
        currimg = img[0+hh*i:hh+hh*i,0+ww*i:ww+ww*i]
        cv2.imshow("w", currimg)
        cv2.waitKey(5000)

def zad8():
    img = cv2.imread('img.png')
    h,w = img.shape
    curr = 0
    while curr < w:
        img[:,10*curr] = [255,255,255]

    cv2.imshow("img", img)
    cv2.waitKey(5000)







if __name__ == "__main__":
    zad7()