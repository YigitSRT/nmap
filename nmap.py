#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Coded By YigitSERT")

print("""

1- Hızlı Tarama

2- Servis Bilgisi

3- İşletim Sistemi Bilgisi

4- Kapsamlı Tarama

5- Normal Tarama

6- Açık Portları Bulma

7- Hızlı Port Taraması

8- FIN Taraması

9- XMAS Taraması

10- Ping Taraması

11- UDP Taraması

12- IDLE Taraması

""")

islemnumarasi = input("Bir İşlem Giriniz: ")

if(islemnumarasi =="1"):
    print("Hızlı Tarama")
    hedefip = input("Hedef Ip'yi Giriniz: ")
    os.system("nmap -Pn " + hedefip)
elif(islemnumarasi =="2"):
    print("Servis Bilgisi")
    hedefip = input("Hedef Ip Numarasini Giriniz: ")
    os.system("nmap -sS -sV -Pn " + hedefip)
elif(islemnumarasi =="3"):
    print("İşletim Sistemi Bilgisi")
    hedefip = input("Hedef Ip Giriniz: ")
    os.system("nmap -O -Pn " + hedefip) 
elif(islemnumarasi =="4"):
    print("Normal Tarama")
    hedefip = input("Hedef Ip Numarasini Giriniz: ")
    os.system("nmap -vv -Pn " + hedefip)
elif(islemnumarasi =="5"):
    print("Genis Tarama")
    hedefip = input("Hedef Ip Numarasini Giriniz: ")
    os.system("nmap -vv -Pn " + hedefip)
elif(islemnumarasi =="6"):
    print("Acik Port Bulma")
    hedefip = input("Hedef Ip Numarasini Giriniz: ")
    os.system("nmap -sT -Pn " + hedefip)
elif(islemnumarasi =="7"):
    print("Hizli Port Tarama")
    hedefip = input("Hedef Ip Numarasini Giriniz: ")
    os.system("nmap -F -Pn " + hedefip)
elif(islemnumarasi =="8"):
    print("FIN Taramasi")
    hedefip = input("Hedef Ip Numarasini Giriniz: ")
    os.system("nmap -sF -v -Pn " + hedefip)
elif(islemnumarasi =="9"):
    print("XMAS Taramasi")
    hedefip = input("Hedef Ip Numarasini Giriniz: ")
    os.system("nmap -sX -v -Pn " + hedefip)
elif(islemnumarasi =="10"):
    print("Ping Taramasi")
    hedefip = input("Hedef Ip Numarasini Giriniz: ")
    os.system("nmap -sP -v -Pn " + hedefip)
elif(islemnumarasi =="11"):
    print("UDP Taramasi")
    hedefip = input("Hedef Ip Numarasini Giriniz: ")
    os.system("nmap -sU -v -Pn " + hedefip)
elif(islemnumarasi =="12"):
    print("IDLE Taramasi")
    hedefip = input("Hedef Ip Numarasi Giriniz: ")
    os.system("nmap -sl -v -Pn " + hedefip)
else:
    print("Yanlis Secim Yaptiniz Program Kapatiliyor...")