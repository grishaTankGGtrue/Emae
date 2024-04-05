from PIL import Image

img1 = Image.open("Line.jpg")

width, height = img1.size

left = (width / 6) * 2.5
top = height / 9
right = (width / 6) * 3.5
bottom = (height / 9) * 8

img2 = img1.crop((left, top, right, bottom))

img2.show()