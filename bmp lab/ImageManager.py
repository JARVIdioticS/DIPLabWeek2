from os import name
from PIL import Image
import numpy as np

class ImageManager:
    width = None
    height = None
    bitDepth = None

    img = None
    data = None
    original = None

    def read(self, fileName):
        global img 
        global data 
        global original 
        global width 
        global height 
        global bitDepth 
        img = Image.open(fileName)
        data = np.array(img)
        original = np.copy(data)
        width = data.shape[0]
        height = data.shape[1]

        mode_to_bpp = {"1":1,"L":8,"P":8,"RGB":24,"RGBA":32,"CMYK":32,"YCbCr":24,"LAB":24,"HSV":24,"I":32,"F":32}
        bitDepth = mode_to_bpp[img.mode]

        print("Image %s with %s x %s pixels (%s bits per pixels) has been read!" % (img.file-name, width, height, bitDepth))

    def write(self, fileName):
        global img 
        img = Image.fromarray(data)
        try:
            img.save(fileName)
        except:
            print("Write file error")
        else:
            print("Image %s has been written!" %(fileName))
