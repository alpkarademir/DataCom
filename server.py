#Alp Furkan Karademir

#server.py

import socket

#Socketin ve portun tanımlanması, bağlanabilecek kullanıcı sayısının belirlenmesi.

PORT = 8080
s = socket.socket()
HOST = socket.gethostname()
s.bind((HOST, PORT))
s.listen(3)
print("Server acildi")

#Döngü sağlandığı süre boyunca tanımlanan dosyayı rb komutu ile bit ayırımı ile yollar.

while True:
    conn, addr = s.accept()
    print("Client baglandi.", addr)
    data = conn.recv(1024)
    print("Server baglandi.", repr(data))

    filename = "alpVeri.txt"
    f = open(filename, "rb")
    l = f.read(1024)
    while (l):
        conn.send(l)
        print("Send ", repr(l))
        l = f.read(1024)
    f.close()

# Gönderim tamamlandı. Dosyanın sonuna isim yazılıp bağlantı sonlanır.

    print("Dosya gonderildi.")
    conn.send(b"Alp Furkan Karademir")
    conn.close()
