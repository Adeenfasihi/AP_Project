import Tkinter as tk
from appJar import gui
from FileDialog import *
import tkFileDialog
import os
#import pathlib

global head,tail

root=tk.Tk()
# fileName=''
class HELLO1:
    def __init__(self, master):
        app = gui("DOCUMENT SCANNER", "1350x710")
        app.setBg("black")
        app.setFont(18)
        self.app = app
        app.addLabel("title", "WELCOME TO THE BINARIZATION OF DOCUMENTS")
        app.setLabelFg("title", "white")
        # app.addButton("BROWSE A FILE",self.press)
        #self.master = master
        #self.var_filename = master
        # self.button_browse = Button(master, text="Browse", command=self.loadtemplate)
        app.addButton("Browse",self.loadtemplate)
        # self.button_browse.pack(side="top")
        app.go()

    def loadtemplate(self,app):
        tk.Tk().withdraw()
        self.app.removeAllWidgets()
        self.app.stop()
        os.system("python binarization.py")


HELLO1(root)


