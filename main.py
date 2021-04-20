import requests
import colorama
import threading
import os
import ctypes
from colorama import Fore, Style
from threading import Thread
from sys import stdout
from requests import Session
from time import strftime, gmtime

sent = 0
session = Session()
b = Style.BRIGHT
os = os.system
os('cls')

ctypes.windll.kernel32.SetConsoleTitleW(f"[REPORT BOT] Advanced Report Tool ")

print(f"""

{b+Fore.GREEN}

| |  HHHHHHHHH     HHHHHHHHH     | |  HHHHHHHHH     HHHHHHHHH     | |    
| |  H:::::::H     H:::::::H     | |  H:::::::H     H:::::::H     | |
| |  HH::::::H     H::::::HH     | |  HH::::::H     H::::::HH     | |
\ /    H:::::H     H:::::H       \ /    H:::::H     H:::::H       \ /
       H::::::HHHHH::::::H              H::::::HHHHH::::::H 
       H:::::::::::::::::H              H:::::::::::::::::H
       H:::::::::::::::::H              H:::::::::::::::::H 
       H::::::HHHHH::::::H              H::::::HHHHH::::::H
| |    H:::::H     H:::::H       | |    H:::::H     H:::::H       | |
| |    H:::::H     H:::::H       | |    H:::::H     H:::::H       | |
| |  HH::::::H     H::::::HH     | |  HH::::::H     H::::::HH     | |
\ /  H:::::::H     H:::::::H     \ /  H:::::::H     H:::::::H     \ /
     H:::::::H     H:::::::H          H:::::::H     H:::::::H
     HHHHHHHHH     HHHHHHHHH          HHHHHHHHH     HHHHHHHHH                   
                                                                                                                                                                    


PS: Must Have Admin On The Server ;)

{b+Fore.RED} x > {Fore.RESET}TO DO: Subscribe and Like 

{b+Fore.RED} x > {Fore.RESET}Options

{b+Fore.RED} {1} > {Fore.RESET}illegal Conent {b+Fore.GREEN}::{Fore.RESET} 1
{b+Fore.RED} {2} > {Fore.RESET}Harrassment {b+Fore.GREEN}::{Fore.RESET} 2
{b+Fore.RED} {3} > {Fore.RESET}Spam or Phishing Links {b+Fore.GREEN}::{Fore.RESET} 3
{b+Fore.RED} {4} > {Fore.RESET}Self harm {b+Fore.GREEN}::{Fore.RESET} 4
{b+Fore.RED} {5} > {Fore.RESET}NSFW Content {b+Fore.GREEN}::{Fore.RESET} 5
""")

token = input(f"{b+Fore.BLUE} > Token{Fore.RESET}: ")
headers = {'Authorization': token, 'Content-Type':  'application/json'}  
r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
if r.status_code == 200:
        pass
else:
        print(f"{b+Fore.RED} > Invalid Token")
        input()
guild_id1 = input(f"{b+Fore.BLUE} > Server ID{Fore.RESET}: ")
channel_id1 = input(f"{b+Fore.BLUE} > Channel ID{Fore.RESET}: ")
message_id1 = input(f"{b+Fore.BLUE} > Message ID{Fore.RESET}: ")
reason1 = input(f"{b+Fore.BLUE} > Option{Fore.RESET}: ")


def Main():
  global sent
  headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36',
        'Authorization': token,
        'Content-Type': 'application/json'
      }

  payload = {
    'channel_id': channel_id1,
    'guild_id': guild_id1,
    'message_id': message_id1,
    'reason': reason1
  }

  while True:
    r = requests.post('https://discord.com/api/v6/report', headers=headers, json=payload)
    if r.status_code == 201:
      print(f"{Fore.GREEN} > Sent Report {b+Fore.BLUE}::{Fore.GREEN} ID {message_id1}")
      ctypes.windll.kernel32.SetConsoleTitleW(f"[REPORT BOT] By Offender | Sent: %s" % sent)
      sent += 1
      
    elif r.status_code == 401:
      print(f"{Fore.RED} > Invalid token")
      input()
      exit()
    else:
      print(f"{Fore.RED} > Error")


print()
for i in range(500, 1000):
    Thread(target=Main).start()
