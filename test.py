import qrcode
from PIL import Image

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)
qr.add_data('https://www.example.com')
qr.make(fit=True)

# Create an image from the QR code
qr_image = qr.make_image(fill_color="black", back_color="white")

# Create an image with a white square
square_size = 1
square_image = Image.new('RGB', (square_size, square_size), (255, 255, 255))

# Resize the square image to be the same size as the QR code
square_image = square_image.resize(qr_image.size)

# Create a new image with the same size as the QR code
result_image = Image.new('RGB', qr_image.size)
square_image = square_image.convert('1')
# Paste the QR code and the square image into the new image
result_image.paste(qr_image, (0, 0))
result_image.paste(square_image, (0, 0), mask=square_image)

# Save the resulting image
result_image.save('qr_code.png')