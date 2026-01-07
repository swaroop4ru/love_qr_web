import qrcode

url = "https://YOUR_GITHUB_USERNAME.github.io/love_qr_web/"
img = qrcode.make(url)
img.save("qr.png")
print("QR generated")
