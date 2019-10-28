#Alp Furkan Karademir

#client.py

import socket

# Ana bağlantının adres tanımlanması ve portun okunması.
HOST = socket.gethostbyname("192.168.1.30")
PORT = 8080
s = socket.socket()

s.connect((HOST, PORT))
s.send(b"Baglandi")

# Alınan dosyanın seçilen isim ile kaydedilmesi. wb komutu ile byte bazında yazılması.

with open('alinandosya.txt', 'wb') as f:
    print("dosya okundu")
    while True:
        print('veri aliniyor')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        f.write(data)

#Dosya alındı. Bağlantı kapanır.

f.close()
print('Dosya alindi.')
s.close()
