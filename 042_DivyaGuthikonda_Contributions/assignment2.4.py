#Write a program to load, open and save an image. 
# (hint : use opencv-python or PIL modules. Research about them on google and youtube)

from PIL import Image
import PIL
imag=Image.open(r"C:\Users\PRASHANTH\OneDrive\Desktop\042_DivyaGuthikonda_Contributions\BTS Taehyung .jpg")
imag=imag.save("v.jpg")
#image was saved in v.jpg 
