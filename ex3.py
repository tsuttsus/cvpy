import cv2 
import numpy as np 

def CalcHighContrast(b):
    out=0
    if b<50:
        out=0
    elif b>205:
        out=255
    else:
        out=int(255/(205-50)*b)
    return out

def HightContrast(img):
    out=np.zeros((img.shape[0],img.shape[1]))

    for j in range(img.shape[0]):
        for i in range(img.shape[1]):
            out[j][i]=CalcHighContrast(img[j][i])
    return out

if __name__=="__main__":
    img=cv2.imread("img.jpg",0)

    outimg=HightContrast(img)

    cv2.imwrite("./img-ex3.jpg",outimg)