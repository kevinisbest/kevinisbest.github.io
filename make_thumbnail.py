from PIL import Image, ImageOps

import os
# filename= os,listdir(".")
# _RAW_DIR = "./jpg"
# dirpath ="/home/esa/Documents/video/video2"

for index in os.listdir("."):
	if os.path.splitext(index)[-1] == '.jpg':
		img = Image.open (index)
		thumb = ImageOps.fit(img, (450, 450), Image.ANTIALIAS)
		thumb.save(index, format="jpeg")
		# img.thumbnail((450,450), resample = Image.ANTIALIAS)
		# img.save( index , format="jpeg")
