from PIL import Image, ImageFilter


chiling = Image.open('resources/chiling.jpg')
width, height = chiling.size
chiling.show()
chiling.transpose(Image.FLIP_LEFT_RIGHT).show()
chiling.filter(ImageFilter.GaussianBlur(4)).show()
chiling.filter(ImageFilter.EMBOSS).show()
chiling.thumbnail((width // 4, height // 4))
chiling.show()
