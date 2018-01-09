from appJar import gui
import os
path = "binarized1.jpg"
# from binarization import img_out
class hello3:
    def press(self,app):
        print "OK"
        os.system("python fifth_page.py")

    def __init__(self):

        app = gui("DOCUMENT SCANNER", "1350x710")
        app.setBg("black")
        app.setFont(15)
        self.app = app
        #os.system("python binarization.py")
        #app.startLabelFrame("Image", 5, 15,colspan=2,rowspan=3)
        # app.addImage("image", "img2.jpg",8,12)
        app.addImage("image", path, 8, 12)
        #app.stopLabelFrame()
        app.addButton("DONE",self.press,9,12)
        app.go()
hello3()

