import os
from PIL import Image

Img_Dir = '/home/davidms/Documents/SLIC-Python/images/'
file_Dir ='/home/davidms/Documents/SLIC-Python/' 
file_dest ='/home/davidms/Documents/SLIC-Python/images_out/'
image_type = '.jpg'

for dirName, subdirList, fileList in os.walk(Img_Dir):
	for fname in fileList:
		#name = os.path.basename(Img_Dir)
		#print(name)
		name = fname.rstrip('.png')
		im = Image.open(Img_Dir+fname)
		bg = im.convert('RGB')
		bg.save(file_dest+name+image_type, qualiaty=100)


