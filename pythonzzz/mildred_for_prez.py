from PIL import Image
# def elections():
choose_image = input("Who should be the president? cat, mildred, nora, broccoli or plant")
        #if choose_image.lower() != "cat" and choose_image.lower() != "mildred" and choose_image.lower() != "nora" and choose_image.lower() != "broccoli" and choose_image.lower() != "plant":
#            elections()
#elections()
im = Image.open(choose_image.lower()+".jpg")
list(im.getdata())
color_intensity = [x[0]+x[1]+x[2] for x in list(im.getdata())]
#def choose_color():
#    which_color = input("purple or prez? ")
#    if which_color == "purple":
#        for n,i in enumerate(color_intensity):
#            if i < 182:
#                color_intensity[n]=(0,0,128)
#            elif i > 182 and i < 364:
#                color_intensity[n]=(153,50,204)
#            elif i < 364 and i < 546:
#                color_intensity[n]=(100,149,237)
#            else:
#                color_intensity[n]=(240,248,255)
#    elif which_color == "prez":
for n,i in enumerate(color_intensity):
    if i < 182:
        color_intensity[n]=(0, 51, 76)
    elif i > 182 and i < 364:
        color_intensity[n]=(217, 26, 33)
    elif i > 364 and i < 546:
        color_intensity[n]=(112, 150, 158)
    else:
        color_intensity[n]=(252, 227, 166)
#    else:
#        choose_color()
#choose_color()
im.putdata(color_intensity)
im.show()
#new_image = Image.new(im.mode, im.size)
#new_image.save("output.jpg", "jpeg")
