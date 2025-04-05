from time import sleep

import cv2
import numpy as np
img = cv2.imread('p.png')


def zad1():

    fh = cv2.flip(img, 1)
    cv2.imshow('poziome', fh)
    cv2.waitKey(0)





def zad2():
    fh = cv2.flip(img, 0)
    cv2.imshow('poziome', fh)
    cv2.waitKey(0)



def zad3():
    fh = cv2.flip(img, -1)
    cv2.imshow('poziome', fh)
    cv2.waitKey(0)


def zad4():

    flipped = cv2.flip(img, 1)
    flipped2 = cv2.flip(flipped, 0)
    flipped3 = cv2.flip(flipped2, -1)
    h = np.hstack([img, flipped])
    v = np.hstack([flipped3, flipped2])
    hw = np.hstack([h,v])
    cv2.imshow('1', hw)
    cv2.waitKey(0)





def zad5():
    h, w = img.shape[:2]
    imagecopy = img.copy()

    half = img[:, w // 2:]

    flipped_half = cv2.flip(half, 1)
    imagecopy[:, w // 2:] = flipped_half

    cv2.imshow('Odbicie fragmentu', imagecopy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def zad6():

    print("Wybierz rodzaj odbicia:")
    print("0 - pionowe")
    print("1 - poziome")
    print("-1 - oba")

    choice = int(input())

    flipped = cv2.flip(img, choice)
    cv2.imshow('Wynik odbicia', flipped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    zad6()