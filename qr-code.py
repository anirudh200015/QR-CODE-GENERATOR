import pyqrcode as pqr
from pyqrcode import QRCode
import png

link= input("enter the link for which The Qr Code is to be created")

# generating Qr code of the link 
url= pqr.create(link)

# saving the Qr code into some file format , svg or png
url.png('MY-QR-CODE.png',scale=10)
print("QR code genrated")