import numpy as np
import cv2

image = cv2.imread("p.jpg")


def zad1():

    M = np.ones(image.shape, dtype="uint8") * 100
    imageNP = cv2.add(image, M)
    cv2.imshow("Lighter", imageNP)

    imageCV = cv2.add(image, 100)
    cv2.imshow("Lighter CV", imageCV)


    cv2.waitKey(0)

def zad2():

    burned_np = np.clip(image.astype(int) + 150, 0, 255).astype(np.uint8)


    burned_cv = cv2.add(image, 150)


    cv2.imshow(' NumPy', burned_np)
    cv2.imshow(' OpenCV', burned_cv)
    cv2.waitKey(0)
def zad3():
    dark_cv = cv2.subtract(image, 80)
    dark_np = np.subtract(image, 80)

    cv2.imshow(' NumPy', dark_np)
    cv2.imshow(' OpenCV', dark_cv)
    cv2.waitKey(0)
def zad4():
    b,g,r = cv2.split(image)
    b = b + 30
    g = g - 20
    r = r + 10
    cv2.merge([b,g,r], image)
    cv2.imshow(' img', image)
    cv2.waitKey(0)
def zad5():
    s1 = cv2.imread("s1.png")
    s2 = cv2.imread("s2.png")

    if s1.shape != s2.shape:
        s2 = cv2.resize(s2, (s1.shape[1], s1.shape[0]))

    diff = cv2.absdiff(s1, s2)
    print(diff)


if __name__ == "__main__":
    zad5()