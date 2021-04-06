import skimage    

from PIL import Image


name = "gb70.png"
im = Image.open(name)
entropy = skimage.measure.shannon_entropy(im)
print(entropy)

im.close()

