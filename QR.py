import qrcode
import time
import io
from PIL import Image


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
        border=4
    )
    qr.add_data('https://www.instagram.com/khachdallak/')
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    icon = Image.open('icons/instagram.png')
    icon = icon.resize(qr_image.size)
    result_image = Image.new('RGB', qr_image.size)

    result_image.paste(icon, (0, 0), mask=icon)
    result_image.paste(qr_image, (0, 0))
    result_image.save('qr_code_with_instagram_icon.png')
with_icon()


