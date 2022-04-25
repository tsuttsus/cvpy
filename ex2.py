import cv2 
import numpy as np 

def Gray2Bin(img,thresh):
    out=np.zeros((img.shape[0],img.shape[1]))

    for j in range(img.shape[0]):
        for i in range(img.shape[1]):
            if img[j][i]>thresh:
                out[j][i]=255
            else:
                out[j][i]=0
    return out

if __name__=="__main__":
    img=cv2.imread("img.jpg",0)
    threshold=128

    outimg=Gray2Bin(img,threshold)

    cv2.imwrite("./img-ex2.jpg",outimg)