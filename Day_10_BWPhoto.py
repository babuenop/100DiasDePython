


from PIL import Image 
color_image = Image.open("image1.jpg")
gray_scale = color_image.convert("1")
gray_scale.save("bw_image_w1.jpg")
gray_scale = color_image.convert("L")
gray_scale.save("bw_image.jpg")







