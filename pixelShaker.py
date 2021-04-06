
from PIL import Image

nameId = "a"
id = 0
tailName = ".png"

for i in range(10):
    name = nameId+str(id)+tailName
    im = Image.open(name)
    pixelMap = im.load()

    img = Image.new( im.mode, im.size)
    pixelsNew = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
	    if 0 in pixelMap[i,j]:
	        if j > 0:
		    if 0 in pixelsNew[i,j-1]:
		        pixelsNew[i,j-1] = (255,255,255,255)
		    else:
		        pixelsNew[i,j-1] = (0,0,0,255)
	        if j < 31:
		    if 0 in pixelsNew[i,j+1]:
		        pixelsNew[i,j+1] = (255,255,255,255)
		    else:
		        pixelsNew[i,j+1] = (0,0,0,255)
	        if i > 0:
		    if 0 in pixelsNew[i-1,j]:
		        pixelsNew[i-1,j] = (255,255,255,255)
		    else:
		        pixelsNew[i-1,j] = (0,0,0,255)
	        if i < 31:
		    if 0 in pixelsNew[i+1,j]:
		        pixelsNew[i+1,j] = (255,255,255,255)
		    else:
		        pixelsNew[i+1,j] = (0,0,0,255)
	    else:
	        pixelsNew[i,j] = pixelMap[i,j]
    im.close()
    id = id + 10
    name = nameId+str(id)+tailName
    img.save(name)
    img.close()
   
