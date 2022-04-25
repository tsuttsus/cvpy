import cv2 
import numpy as np 

def CalcLowContrast(b):
    # 75~180
    outb=int((180-75)/255*b)
    return outb

def LowContrast(img):
    out=np.zeros((img.shape[0],img.shape[1]))

    for j in range(img.shape[0]):
        for i in range(img.shape[1]):
            out[j][i]=CalcLowContrast(img[j][i])
    return out

if __name__=="__main__":
    img=cv2.imread("img.jpg",0)

    outimg=LowContrast(img)

    cv2.imwrite("./img-ex4.jpg",outimg)