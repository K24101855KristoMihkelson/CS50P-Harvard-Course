from PIL import Image, ImageOps
import sys

if len(sys.argv) != 3:
    sys.exit("Usage: python shirt.py input output")

input_file, output_file = sys.argv[1], sys.argv[2]
if input_file.split(".")[-1].lower() != output_file.split(".")[-1].lower():
    sys.exit("Input and output have different extensions")

shirt = Image.open("shirt.png")
size = shirt.size
image = Image.open(input_file)
image = ImageOps.fit(image, size)
image.paste(shirt, shirt)
image.save(output_file)
