# Importing library
import qrcode

website = input("Website: ")
data = website
img = qrcode.make(data)

name = input("Image name: ")
png_or_svg = input("png or svg? ")
img.save(f'{name}.{png_or_svg}')
print("QR code saved to " + name + "." + png_or_svg)