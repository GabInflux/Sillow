import requests
from pystyle import Colorate, Colors, Center
from os import system
from time import sleep

boucle1 = True

header_final = """
███████╗██╗██╗     ██╗      ██████╗ ██╗    ██╗
██╔════╝██║██║     ██║     ██╔═══██╗██║    ██║
███████╗██║██║     ██║     ██║   ██║██║ █╗ ██║
╚════██║██║██║     ██║     ██║   ██║██║███╗██║
███████║██║███████╗███████╗╚██████╔╝╚███╔███╔╝
╚══════╝╚═╝╚══════╝╚══════╝ ╚═════╝  ╚══╝╚══╝ 
  V 1.0 - Gab_#8440 - discord.gg/BtNrFc45B7\n\n\n\n"""

while boucle1:
    system('cls')
    print(Colorate.Diagonal(Colors.purple_to_blue, Center.XCenter(header_final)))
    print(Colorate.Horizontal(Colors.purple_to_blue, "[?] Webhook URL ↓"))
    webhook_url = input("")
    if webhook_url.startswith("https://discord.com/api/webhooks/"):
        try:
            system('cls')
            requests.delete(webhook_url.rstrip())
            print(Colorate.Diagonal(Colors.purple_to_blue, Center.XCenter(header_final)))
            print(Colorate.Horizontal(Colors.purple_to_blue, "Webhook deleted !"))
            sleep(5)
        except:
            system('cls')
            print(Colorate.Diagonal(Colors.purple_to_blue, Center.XCenter(header_final)))
            print(Colorate.Horizontal(Colors.yellow_to_red, "[!] Error on deleting the webhook."))
            sleep(2)
    else:
            system('cls')
            print(Colorate.Diagonal(Colors.purple_to_blue, Center.XCenter(header_final)))
            print(Colorate.Horizontal(Colors.yellow_to_red, "[!] Please insert a valid link."))
            sleep(2)