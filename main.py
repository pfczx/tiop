import cv2


def zad1():
    image = cv2.imread('images.jpeg')
    cv2.imshow("zad1", image)
    pixel00=image[0,0]
    cv2.waitKey(0)
    print(f'Pixel b g r  '+str(pixel00))
def zad2():
    image = cv2.imread('images.jpeg')
    image[-1,-1]=(0,0,255)
    print(str(image[-1,-1]))
def zad3():
    image = cv2.imread('images.jpeg')
    h,w,x = image.shape
    center_pixel = image[int(h//2),int(w//2)]
    print(center_pixel)
def zad4(x,y):
    image = cv2.imread('images.jpeg')
    h,w,x = image.shape
    if x < 0 or y <0 or x > h or y > w:
        return "Invalid x or  y"
    image[x,y] = (0,0,0)
    print(image[x,y])
def zad5():
    image = cv2.imread('images.jpeg')
    h, w, x = image.shape
    image[0:h//2,0:w//2]=(255,0,0)
    cv2.imshow("zad5", image)
    cv2.waitKey(0)
def zad6():
    image = cv2.imread('images.jpeg')
    h, w, x = image.shape
    center = (h//2,2//2)
    image[center[0]-100:center[1]-100,center[1]+100:center[0]+100]=(0,0,255)
    cv2.imshow("zad6", image)
    cv2.waitKey(0)






if __name__=="__main__":
    zad6()