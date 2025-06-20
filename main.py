import cv2
import numpy as n
import matplotlib.pyplot as plt

def zad1():



    # Załadowanie obrazu
    image = cv2.imread('sample_image.jpg')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Konwersja z BGR na RGB

    ## Zadanie 1: Eksploracja różnych metod rozmycia
    # a. Stosujemy cztery różne metody rozmycia

    # i. Proste rozmycie
    blur_simple = cv2.blur(image, (5, 5))

    # ii. Rozmycie Gaussa
    blur_gaussian = cv2.GaussianBlur(image, (5, 5), 0)

    # iii. Rozmycie medianowe
    blur_median = cv2.medianBlur(image, 5)

    # iv. Rozmycie dwustronne
    blur_bilateral = cv2.bilateralFilter(image, 9, 75, 75)

    # Wyświetlenie wyników
    plt.figure(figsize=(20, 10))
    plt.subplot(2, 3, 1), plt.imshow(image), plt.title('Oryginał')
    plt.subplot(2, 3, 2), plt.imshow(blur_simple), plt.title('Proste rozmycie')
    plt.subplot(2, 3, 3), plt.imshow(blur_gaussian), plt.title('Rozmycie Gaussa')
    plt.subplot(2, 3, 4), plt.imshow(blur_median), plt.title('Rozmycie medianowe')
    plt.subplot(2, 3, 5), plt.imshow(blur_bilateral), plt.title('Rozmycie dwustronne')
    plt.show()
if __name__ == '__main__':


