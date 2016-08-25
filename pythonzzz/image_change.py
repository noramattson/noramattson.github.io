from PIL import Image

darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

im = Image.open("nora.jpg")

data = im.getdata()
data_list = list(data)
#print(len(data_list))
def colorize(image_data):
	new_pic = []
	for pixel in image_data:
		red = pixel[0]
		green = pixel[1]
		blue = pixel[2]
		total = red + green + blue
		if total < 182:
			new_pic.append(darkBlue)
		elif total > 182 and total < 364:
			new_pic.append(red)
		elif total > 364 and total < 536:
			new_pic.append(lightBlue)
		else:
			new_pic.append(yellow)
	return new_pic

data_colorized = colorize(data_list)
print("Colorized data length:{}".format(len(data_colorized)))
pic = Image.new(im.mode, im.size)
pic.putdata(data_colorized)
pic.show()
#pic.save("output.jpg","jpeg")
