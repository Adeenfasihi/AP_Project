from PIL import Image
import os
import cv2
import numpy as np
from appJar import gui
import tkFileDialog
global in_path,hello

class binarize:
	def __init__(self, app):
		print "he"
		self.app = app
		self.app.removeAllWidgets()
		self.app.setBg("black")
		self.app.setFont(15)
		global head
		global tail
		in_path = tkFileDialog.askopenfilename()
		print(in_path)
		head, tail = os.path.split(in_path)
		# app.startLabelFrame("Image", 5, 10)
		self.app.addImage("image", tail, 5, 10)
		# app.stopLabelFrame()
		self.app.addButton("BINARIZE", self.press, 7, 10)


	def press(self,app):
		img = cv2.imread(tail,0)

		rows,cols = img.shape

		size_w = 15
		k = 0.2
		R = 128
		print "binary"
		#hist = np.histogram(img, bins=256)
		img_out = np.ones((rows,cols),dtype=int)*255
		#avg = np.mean(img)

		i = int(size_w/2)
		for r in range(i,rows-i):
			for c in range(i,cols-i):
				crop_img = img[r-i:r+i,c-i:c+i]

				u = np.mean(crop_img)
				o = np.std(crop_img)
				thr = u*(1+(k*((o/R)-1)))

		#		if (img[r][c] >= thr or u < avg):
				if (img[r][c] >= thr):
					img_out[r][c] = 255
				else:
					img_out[r][c] = 0

		#bin_counts, bin_edges, patches = plt.hist(img.ravel(), 256)
		#plt.show()
		print "hi"
		cv2.imwrite("binarized1.jpg", img_out)
		im = Image.open("binarized1.jpg")
		print "bye"
		im.show()
		#os.system("python third_page.py")


if __name__ == '__main__':
    app = gui("DOCUMENT SCANNER", "1350x710")

    # hello2(app)
    hello=binarize(app)
    app.go()

