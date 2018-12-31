'''
打开图片
'''
# from PIL import Image
#
# image = Image.open("P:\\Users\\jared\\Documents\\4.jpg")
# print(image.format, image.size, image.mode)
# image.show()

'''
抠图，上述代码讲图片的((600, 300), (600, 660), (1050, 300), (1050, 660))所画出来的区域进行裁剪，并保存在cutting.jpg中
'''
# from PIL import Image
# image = Image.open("P:\\Users\\jared\\Documents\\4.jpg")
# print(image.format, image.size, image.mode)
# box = (600, 300, 1050, 660)
# region = image.crop(box)
# region.save("cutting.jpg")

'''
图片拼合，把头像照片截取出来，然后调换头像照片180度，然后在拼接在一起，
'''
from PIL import Image
image = Image.open("P:\\Users\\jared\\Documents\\4.jpg")
print(image.format, image.size, image.mode)
box = (600, 300, 1050, 660)
egion = image.crop(box)
#egion.save("cutting.jpg")


region = egion.transpose(Image.ROTATE_180)
image.paste(region, box)
image.show()
