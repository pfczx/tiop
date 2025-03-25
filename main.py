import cv2
import imutils


def zad1():
    image = cv2.imread('./e.jpg')
    height, width = image.shape[:2]
    resized = cv2.resize(image, (height//2, width//2), interpolation=cv2.INTER_AREA)
    cv2.imshow("Resized", resized)
    cv2.waitKey()
def zad2():
    image = cv2.imread('./e.jpg')
    height, width = image.shape[:2]
    resized = cv2.resize(image, (height*2, width*2), interpolation=cv2.INTER_LINEAR)
    cv2.imshow("Resized", resized)
    cv2.waitKey()
def zad3():
    image = cv2.imread('./e.jpg')
    resized = cv2.resize(image, (200, 200), interpolation=cv2.INTER_LANCZOS4)
    cv2.imshow("Resized", resized)
    cv2.waitKey(3000)


def zad4():
    image = cv2.imread('./e.jpg')
    resized1 = cv2.resize(image, (200, 200), interpolation=cv2.INTER_LANCZOS4)
    resized2 = cv2.resize(image, (200, 200), interpolation=cv2.INTER_LINEAR)
    resized3 = cv2.resize(image, (200, 200), interpolation=cv2.INTER_CUBIC)
    resized4 = cv2.resize(image, (200, 200), interpolation=cv2.INTER_NEAREST)
    cv2.imshow("Resized1 lancos4", resized1)
    cv2.imshow("Resized2 linear" , resized2)
    cv2.imshow("Resized3 cubic", resized3)
    cv2.imshow("Resized4 nearest ", resized4)

    cv2.waitKey(30000)

def zad5():
    image = cv2.imread('./e.jpg')
    resized = imutils.resize(image, width=500,inter=cv2.INTER_NEAREST)
    cv2.imshow("Resized1", resized)
    cv2.waitKey(3000000)
def zad6():
    image = cv2.imread('./e.jpg')
    resized = imutils.resize(image, height=400,inter=cv2.INTER_NEAREST)
    cv2.imshow("Resized1", resized)
    cv2.waitKey(3000000)

def zad7():
    image = cv2.imread('./e.jpg')
    resized = imutils.resize(image, width=image.shape[1]//5,inter=cv2.INTER_AREA)
    cv2.imshow("Resized1 ", resized)
    cv2.waitKey(3000000)

def zad8():
    image = cv2.imread('./e.jpg')
    resized = imutils.resize(image, width=image.shape[1]*4,inter=cv2.INTER_LANCZOS4)
    resized1 = imutils.resize(image,width=image.shape[1]*4,inter=cv2.INTER_CUBIC)
    cv2.imshow("Resized1 ", resized)
    cv2.imshow("Resized2",resized1)
    cv2.waitKey(3000000)
def zad9():
    img = cv2.imread('./e.jpg')

    for i in range(1,10):
        newsize = int(img.shape[1] * (1 + 0.2 * i))
        image = cv2.imread('./e.jpg')
        resized = imutils.resize(image, width=newsize, inter=cv2.INTER_LANCZOS4)
        cv2.imshow("Resized1 ", resized)
        cv2.waitKey(1000)

def zad10():
    img = cv2.imread('./e.jpg')
    resized = imutils.resize(img, width=800)
    cv2.imwrite('nowy.jpg', resized)


if __name__=="__main__":
    zad10()