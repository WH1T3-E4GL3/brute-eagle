import os
import instaloader
from getpass import getpass
import time
import subprocess as sub
import random

# password+ banner
os.system("clear")
print('''\033[95m 
         _
        //	☁             ｡⋆｡ ﾟ    ☾ ﾟ｡⋆
       ||              |\_/|   
        \\\  .-""""-._.' - -(    ˚　　　　✦　　　.　　. 　 ˚　.　　　　
         \\\/          \ =_T/=
          \    \       /`"`  　.   　　˚　　 　　*　　 　　✦　　
           \   | /    |          ⋆  ｡ﾟ  ☁︎
           /  / -\   /
           `\ \\\  | ||     meow meow zhoi
 Brutal	     \_)) |_))         .　　. 　 ˚　.
                                           *　　 　　✦　　
\033[0m''')
os.system('figlet Brute Eagle | lolcat')   
passwd = input(
    "\033[1m\033[94m[❖] \033[1m\033[91mEnter Tool PassWord \033[90m➣  ")
passwd = passwd.lower()
if passwd == 'we':
    time.sleep(5)
    print("\033[92m[✓] login sucessfull")
    time.sleep(0.4)
    print("Loading....")
    os.system("clear")
    print('\n')

else:
    print("\033[93m[!]  \033[91m\033[1mPassword Wrong! ")
    print("\033[36m[!]  \033[1mContact Devolopers")
    time.sleep(4)
    os.system("xdg-open http://api.whatsapp.com/send?phone=+91(9072233245)&text=I_Need_Password_for_Zhoi-Insta_Rate_200Rs_Ok")
    exit()


# BANNER educational purposes
print('''\033[95m 
         _
        //	☁             ｡⋆｡ ﾟ    ☾ ﾟ｡⋆
       ||              |\_/|   
        \\\  .-""""-._.' - -(    ˚　　　　✦　　　.　　. 　 ˚　.　　　　
         \\\/          \ =_T/=
          \    \       /`"`  　.   　　˚　　 　　*　　 　　✦　　
           \   | /    |          ⋆  ｡ﾟ  ☁︎
           /  / -\   /
           `\ \\\  | ||     meow meow zhoi
 Brutal	     \_)) |_))         .　　. 　 ˚　.
                                           *　　 　　✦　　
\033[0m''')
os.system('figlet Brute Eagle | lolcat') 


class bcolors:
    BOLD = '\033[1m'
    PURPLE = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[95m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'


def start():

    sceltadisc = input(
        "\033[93m\033[1m\n\n[!]Use this program  for educational purposes only? [y/n]: ")

    if sceltadisc == "y":
        print("\n")
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
		   `\ \\\  | ||     mew mew zhoi
	 Brutal	     \_)) |_))


	\033[0m''')
    else:
        os.system("xdg-open 'https://instagram.com/mr_lalu_1232/")
        os.system("clear")
        print("\t  [#] Insta cyber_st4rk\t")
        print("\t  [#]Whatsapp : S74RK\t")

        exit()


def acquisizione():
    while True:
        if veri_break == "si":
            break
        USER = ""
        USER = input(
            '\033[1m\033[92m[?]ENTER INSTAGRAM USERNAME FOR CRACK PASSWORD: ')
        wl = input("[?]Enter the PassList along The Path: ")
        sleepp = int(
            input("\033[1m\033[91m\n[!]Type the sleep time for login(sec) (Rec:900): "))
        while True:
            sub.call("clear")
            procedere = input("Username to bruteforce = "+USER+"\n\nWordlist = "+wl+"\n\nSleep time = " +
                              str(sleepp)+bcolors.WARNING+"\n\nProoceding? [y/break/modify]: "+bcolors.ENDC)
            if procedere == "y":
                veri_break = "si"
                break
            elif procedere == "modify":
                print("\nReturn...")
                break
            elif procedere == "break":
                exit()
            else:
                pass

