from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filtered_image = img.filter(ImageFilter)
