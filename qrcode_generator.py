import qrcode

data = input("Enter text or number to convert to QR code: ")

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="pink")
img.save("qrcode.png")

print("QR code generated and saved as qrcode.png")
