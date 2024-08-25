import qrcode

# taking UPI ID as a input
upi_id = input("enter your upi id = ")

# upi://pay?pa=upi_ID&pn=NAME$am=Amount$cu=CURRENCY&tn=MESSAGE

# define the payment url based on the upi an the payment app
# you can modify these URLs based on the payment app you wnat to support

phonepe_url = f'upi:pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi:pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi:pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# creatq qr code for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# save the QR code to image file(opctional)
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

# display the QR codes (you may need to install PIL/PILLOW library)
phonepe_qr.save()
paytm_qr.save()
google_pay_qr.save()