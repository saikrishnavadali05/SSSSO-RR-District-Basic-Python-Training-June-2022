#4.Write a program to load, open and save an image. (hint : use opencv-python or PIL modules. Research about them on google and youtube)
from PIL import Image
import PIL
ig = Image.open(r"C:\Users\SRIKANTH\Desktop\0001.jpg")
ig.show()
ig = ig.save("srikanth.jpg")