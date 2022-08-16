import qrcode
text_generate=input("Enter Text What you make QRcode :) ")
file_name=input("Enter File Name  with Extension")
d=qrcode.make(text_generate)
d.save(file_name)

#Code By Shuvo Kumar Saha 


