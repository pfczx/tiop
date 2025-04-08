import cv2
image = cv2.imread("1.png")

def zad1():
    (B,G,R)= cv2.split(image)
    cv2.imshow("B",B)
    cv2.imshow("G",G)
    cv2.imshow("R",R)
    cv2.waitKey(0)
def zad2():
    image = cv2.imread("color.png")
    (B,G,R)= cv2.split(image)
    cv2.imshow("org",image)
    cv2.imshow("B",B)
    cv2.imshow("G",G)
    cv2.imshow("R",R)#nie widac kolorow na swietrze
    cv2.waitKey(0)
def zad3():
    image = cv2.imread("color.png")
    (B,G,R)= cv2.split(image)
    image = cv2.merge([R,G,B])
    B = cv2.bitwise_not(B)
    image2 = cv2.merge([B,G,B])
    cv2.imshow("zamiana",image)
    cv2.imshow("zerowanie",image2)
    cv2.waitKey(0)
def zad4():
    image = cv2.imread("color.png")
    (B,G,R)= cv2.split(image)
    B = cv2.add(B,255)
    image = cv2.merge([B,G,R])
    cv2.imshow("zamiana",image)
    cv2.waitKey(0)
def zad5():
    
if __name__ == "__main__":
    zad4()