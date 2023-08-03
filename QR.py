import qrcode
import time
import io
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
from skimage.feature import canny

def simple_qr_code(message):
    img = qrcode.make(message, error_correction=qrcode.constants.ERROR_CORRECT_H,
                      box_size=10, border=2)
    # buffer
    buf = io.BytesIO()
    img.save(buf, format='png')
    buf.seek(0)
    return buf


def with_icon():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1
    )
    qr.add_data('https://www.instagram.com/khachdallak/')
    qr.make(fit=True)
    # (123, 31, 162) purple
    qr_image = qr.make_image(fill_color=(123, 31, 162), back_color="white")
    qr_image.save('qr_code_with_instagram_icon.png')


def round_corners(input, output):
    image = Image.open(input)

    # Convert the image to grayscale
    gray_image = image.convert('L')

    # Apply the Canny edge detection algorithm to the grayscale image
    edges = canny(np.array(gray_image), sigma=5)

    # Convert the edges image to a NumPy array
    edge_coords = np.argwhere(edges == True)



    # Draw rounded edges over the detected edges
    radius = 1.5
    draw = ImageDraw.Draw(image)
    for x, y in edge_coords:
        draw.arc((x - radius, y - radius, x + radius, y + radius), 0, 360, fill=(123, 31, 162))

    # Save the modified image
    image.save(output)


round_corners('qr_code_with_instagram_icon.png', 'output.png')


