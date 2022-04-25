import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

def MakeHist(img):
    brightlist=[0]*256
    for j in range(img.shape[0]):
        for i in range(img.shape[1]):
            brightlist[img[j][i]]=brightlist[img[j][i]]+1
    
    return np.array(brightlist)


if __name__=="__main__":
    img=cv2.imread("img.jpg",0)

    data=MakeHist(img)
    var=np.array([x for x in range(0,256)])

    fig=plt.figure()
    plt.bar(var,data,width=1.0)
    plt.title("Brightness")
    plt.xlabel("Gradation")
    plt.ylabel("Number")
    plt.show()

    fig.savefig("img-ex5.jpg")
