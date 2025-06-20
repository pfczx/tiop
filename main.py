import cv2
import numpy as np
import matplotlib.pyplot as plt

def zadanie1_erozja(image_path):
    image = cv2.imread(image_path, 0)
    _, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    kernel_square = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

    eroded_square = cv2.erode(binary, kernel_square, iterations=1)
    eroded_ellipse = cv2.erode(binary, kernel_ellipse, iterations=1)

    cv2.imshow("Original", binary)
    cv2.imshow("Eroded - Square", eroded_square)
    cv2.imshow("Eroded - Ellipse", eroded_ellipse)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def zadanie2_dylatacja(image_path):
    image = cv2.imread(image_path, 0)
    _, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3, 3), np.uint8)
    iterations = [1, 2, 3, 4]

    thicknesses = []
    for i in iterations:
        dilated = cv2.dilate(binary, kernel, iterations=i)
        thickness = np.sum(dilated == 255)
        thicknesses.append(thickness)
        cv2.imshow(f"Dylatacja {i}x", dilated)

    plt.plot(iterations, thicknesses)
    plt.title("Zmiana grubości obiektów w zależności od liczby iteracji")
    plt.xlabel("Liczba iteracji")
    plt.ylabel("Liczba pikseli 255")
    plt.grid()
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def zadanie3_otwarcie(image_path):
    image = cv2.imread(image_path, 0)
    noisy = cv2.medianBlur(image, 5)
    kernel_sizes = [(3, 3), (5, 5), (7, 7)]

    cv2.imshow("Original (with noise)", noisy)
    for size in kernel_sizes:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, size)
        opened = cv2.morphologyEx(noisy, cv2.MORPH_OPEN, kernel)
        cv2.imshow(f"Opening - Kernel {size}", opened)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def zadanie4_zamkniecie(image_path):
    image = cv2.imread(image_path, 0)
    _, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    kernels = {
        "Rect": cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)),
        "Ellipse": cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    }

    cv2.imshow("Original", binary)
    for name, kernel in kernels.items():
        closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
        cv2.imshow(f"Zamknięcie - {name}", closed)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def zadanie5_porownanie(image_path):
    image = cv2.imread(image_path, 0)
    _, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    shapes = {
        "Rect": cv2.MORPH_RECT,
        "Cross": cv2.MORPH_CROSS,
        "Ellipse": cv2.MORPH_ELLIPSE
    }

    operations = {
        "Erozja": cv2.MORPH_ERODE,
        "Dylatacja": cv2.MORPH_DILATE,
        "Otwarcie": cv2.MORPH_OPEN,
        "Zamknięcie": cv2.MORPH_CLOSE,
        "Gradient": cv2.MORPH_GRADIENT
    }

    for shape_name, shape in shapes.items():
        kernel = cv2.getStructuringElement(shape, (5, 5))
        print(f"\nElement: {shape_name}")
        for op_name, op in operations.items():
            result = cv2.morphologyEx(binary, op, kernel)
            cv2.imshow(f"{op_name} - {shape_name}", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def zadanie6_realny_przypadek(image_path):
    image = cv2.imread(image_path, 0)
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    _, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    processed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

    cv2.imshow("Original", image)
    cv2.imshow("Binarized", binary)
    cv2.imshow("After Morph Close", processed)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    path_shapes = "ksztalty.png"
    path_lines = "linie.png"
    path_noise = "noise.png"
    path_letters = "litery.png"
    path_generic = "gene.png"
    path_real = "blachy.jpg"

    zadanie1_erozja(path_shapes)
    zadanie2_dylatacja(path_lines)
    zadanie3_otwarcie(path_noise)
    zadanie4_zamkniecie(path_letters)
    zadanie5_porownanie(path_generic)
    zadanie6_realny_przypadek(path_real)

if __name__ == "__main__":
    main()
