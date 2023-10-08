import qrcode

def url_to_QR(url):
    image = qrcode.make(url)
    return image.save('QR_Code.png')
