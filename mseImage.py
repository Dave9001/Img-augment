from PIL import Image

img1 = Image.open("g.png")
pixelMapImg_1 = img1.load()

img2 = Image.open("gb0.png")
pixelMapImg_2 = img2.load()


def MSE(img1, img2):
    size1 = img1.size
    size2 = img2.size

    if size1[0] != size2[0]:
        print("rozny rozmiar obrazkow")
        exit()
    elif size1[1] != size2[1]:
        print("rozny rozmiar obrazkow")
        exit()

    pmImg1 = img1.load()
    pmImg2 = img2.load()

    N = size1[0] * size1[1]
    mse = 0.0
    for i in range(size1[0]):
        for j in range(size1[1]):
            mse = mse + (pmImg1[i,j] - pmImg2[i,j])

    mse = mse * (1.0/N)

    print(mse)


MSE(img1, img2)

img1.close()
img2.close()

