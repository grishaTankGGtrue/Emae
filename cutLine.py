from PIL import Image

img1 = Image.open("Line.png")

width, height = img1.size

left = (width / 6) * 2.8
top = (height / 9) * 2.35
right = (width / 6) * 3.2
bottom = (height / 9) * 6.6

img2 = img1.crop((left, top, right, bottom))

img2.show()
img2.save("Line.png")