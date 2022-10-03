from PIL import Image

STRIPE_WIDTH = 16

im = Image.open("./output.png")
px = im.load()

x = 0

w, h = im.size
print('width: ', w)

inc = 0
while x != w:
	cordinate = x, 0
	if im.getpixel(cordinate) == (0, 0, 0):
		print("1", end="")
	else:
		print("0", end="")
	if (inc == 7):
		print(" ", end="")
		inc = 0
	x += STRIPE_WIDTH
	inc += 1
print()