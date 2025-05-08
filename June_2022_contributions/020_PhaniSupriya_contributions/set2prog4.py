# Prog to load, open, save an image using PIL Modules

from PIL import Image
img = Image.open("sai.jpg")
img.show()
img = img.save("D:/images/ShirdiSai.jpg")