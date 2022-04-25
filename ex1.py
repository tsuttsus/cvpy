import cv2 
import numpy as np 

# Algorithm
# Brightness=0.299*R+0.587*G+0.114*B;
def Color2Gray(img):
    out=np.zeros((img.shape[0],img.shape[1]))

    for j in range(img.shape[0]):
        for i in range(img.shape[1]):
            b=img[j][i][0]
            g=img[j][i][1]
            r=img[j][i][2]
            gray=0.299*r+0.587*g+0.114*b
            out[j][i]=gray
    return out

if __name__=="__main__":
    img=cv2.imread("img.jpg",1)
    outimg=Color2Gray(img)

    cv2.imwrite("./img-ex1.jpg",outimg)
    