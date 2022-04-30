


from PIL import Image 
im = Image.open("image1.jpg")
# la siguiente linea devuelve los atributos de la imagen. 

print(im.format, im.size, im.mode)

#gray_scale = color_image.convert("1")
#gray_scale.save("bw_image_w1.jpg")
#gray_scale = color_image.convert("L")
#gray_scale.save("bw_image.jpg")







