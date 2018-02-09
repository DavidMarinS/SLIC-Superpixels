# import the necessary packages
import os
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
from skimage import io

Img_Dir = '/home/davidms/Documents/SLIC-Python/images_out/'
file_dest = '/home/davidms/Documents/SLIC-Python/images_slic/'
image_type = '.png'

for dirName, subdirList, fileList in os.walk(Img_Dir):
	for fname in fileList:
		name = fname.rstrip('.jpg')
		image = img_as_float(io.imread(Img_Dir+fname))
		segments = slic(image, n_segments = 5000, compactness=10)
		img_super= mark_boundaries(image, segments)
		io.imsave(file_dest+name+image_type,img_super)


