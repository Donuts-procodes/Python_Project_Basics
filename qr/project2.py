import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=20,border=2)
qr.add_data("https://donuts-procodes.github.io/PersonalWebPortfolio.github.io/") 
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="white")
img.save("donutprofile_qr.png")