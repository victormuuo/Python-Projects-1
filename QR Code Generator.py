#install all the libraries needed
#create a text that collects a text and converts it to a qrcode
#save the qrcode as an image
#create a function that takes the image and converts it to a text

import qrcode

def generate_qrcode(text):

    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=5,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img=qr.make_image(fill_color="black",back_color="white")
    img.save=("qrimg002.png")

url=input("Enter url:")
generate_qrcode(url)    