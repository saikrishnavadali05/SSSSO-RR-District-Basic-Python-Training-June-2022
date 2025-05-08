# Write a program to load, open and save an image.

# Using Python Image Library Package
from PIL import Image

with Image.open("ironman.jpg") as image:

    width, height = image.size

    # Resizing and Rotating the image.
    image = image.resize((width//10, height//10))
    image = image.rotate(180)
    
    # Saving edited image with a new name.
    image.save("edited-ironman.jpg",)

    # print(image.histogram()) - Can be used to print a histogram of the image.