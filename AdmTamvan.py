import sys
import os
print "Welcome To FScript Builder V.2"

os.system(" figlet KEDUT TAMVAN")

title = raw_input(" Title : ")
bg = raw_input(" Background Color : ")
gambar = raw_input(" Url Gambar : ")
warna = raw_input(" Warna Nick : ")
nick = raw_input(" Nick : ")
color = raw_input(" Warna Pesan : ")
pesan = raw_input(" Pesan : ")
marquee = raw_input(" Marquee : ")

teks = "<html>\n<head>\n<title> {}</title>\n</head>\n<body bgcolor='{}'>\n<center><br><img src=' {} ' width='400px' height='400px'><br><font color='{}' size='20'> {}</font>\n<br><br>\n<font color='{}' size='5'> {}</font>\n<br><br><br><br><marquee bgcolor='white'><font color='black' size='4'>{}</marquee></body></html>".format(title, bg , gambar , warna , nick , color , pesan , marquee)

file_bio = open("hasil.html", "w")

file_bio.write(teks)

file_bio.close()
