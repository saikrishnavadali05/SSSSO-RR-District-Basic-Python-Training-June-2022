# PIL python imaging library
# installed PIL using command C:\Python310\python.exe -m pip install --upgrade pip
# importing PIL
from PIL import Image
# opening the image
im = Image.open(r"C:\Users\Admin\Downloads\Amma.jpg")
# displaying the image
im.show()
# saving image
im1 = Image.save("maa.jpg")
