from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

import numpy as np
import cv2



def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err

def compare_image(imageA, imageB, title):
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m,s))

    ax = fig.add_subplot(1,2,1)
    plt.imshow(imageA, cmap = plt.cm.gray)
    plt.axis("off")
    
    ax = fig.add_subplot(1,2,2)
    plt.imshow(imageB, cmap = plt.cm.gray)
    plt.axis("off")

    plt.show()

img_1 = cv2.imread("g.png") 
img_2 = cv2.imread("gb0.png") 

img_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY) 
img_2 = cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY) 

compare_image(img_1, img_2, "basic")

fig = plt.figure("title", figsize=(3,20))
gs = gridspec.GridSpec(6, 2, width_ratios=[1, 1]) 


id = 0
for i in range(10,70,10):
    name_1 = "out"+str(i)+".png"
    name_2 = "gb"+str(i)+".png"
    imageA = cv2.imread(name_1) 
    imageB = cv2.imread(name_2) 

    imageA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY) 
    imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY) 

    #compare_image(img_1, img_2, str(i))

    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)
   

    ax = fig.add_subplot(gs[id])
    plt.imshow(imageA, cmap = plt.cm.gray)
    plt.axis("off")
    ax.title.set_text("%d MSE: %.2f, SSIM: %.2f" % (i,m,s))

    id = id + 1

    ax = fig.add_subplot(gs[id])
    plt.imshow(imageB, cmap = plt.cm.gray)
    plt.axis("off")
    
    id = id + 1
    
    ax.title.set_text("%d MSE: %.2f, SSIM: %.2f" % (i,m,s))



plt.show()
