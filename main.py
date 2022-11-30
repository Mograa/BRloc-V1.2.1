from colorama import Fore
import requests
import pprint
from time import sleep
import os
from passwordgenerator import pwgenerator
from faker import Faker
import socket
import sys
import time

color_1 = Fore.BLUE
color_2 = Fore.RED
color_3 = Fore.MAGENTA
color_4 = Fore.GREEN
color_5 = Fore.WHITE
color_6 = Fore.CYAN
color_7 = Fore.YELLOW

user = 'root'
password = 'root'
user_input = str(input(f'{color_6}User{color_2}>'))
password_input = str(input(f'{color_6}Password{color_2}>'))


sleep(1)
os.system('cls')

clock = time.strftime('%H:%M:%S')


def logo():
    main_logo = f"""
    {color_4}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    
                    {color_4}██████╗ ██████╗ ██╗      ██████╗  ██████╗   
                    {color_4}██╔══██╗██╔══██╗██║     ██╔═══██╗██╔════╝   
                    {color_7}██████╔╝██████╔╝██║     ██║   ██║██║         
                    {color_7}██╔══██╗██╔══██╗██║     ██║   ██║██║        
                    {color_1}██████╔╝██║  ██║███████╗╚██████╔╝╚██████╗   
                    {color_1}╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ 
                                                                 
    {color_7}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
                {color_5}Credits: {color_4}Mogra#3124 | {color_4}github.com/Mograa
    """
    print(main_logo)


def menu():
    main_menu = f"""
   {color_2}[1] {color_6}GeoIP         {color_2}[5] {color_6}FakeAddr          {color_2}[9] {color_6} Portscan           
   {color_2}[2] {color_6}Ping          {color_2}[6] {color_6}Speedtest         {color_2}[10] {color_6}Traceroute                              
   {color_2}[3] {color_6}[off air]     {color_2}[7] {color_6}Domain lookup     {color_2}[11] {color_6}Backup files                               
   {color_2}[4] {color_6}FakeN         {color_2}[8] {color_6}Flush DNS cache   {color_2}[12] {color_6}Installer
    
    
    {color_7}V{color_4}1{color_5}.{color_7}2{color_5}.{color_6}1 {color_5}| {color_5}Entry time: {color_4}{clock} {color_5} | [{color_4}0{color_5}]{color_6}Exit
"""
    print(main_menu)


def returnf():
    print('\n')
    print(f'{color_5}▀' * 81)
    sleep(1)
    main()


def returnins():
    logo_installer()
    installer()


def otheroption():
    print('the selected option does not exist')
    sleep(2)
    os.system('cls')
    returnf()


def req_ip():
    try:
        sleep(0.5)
        os.system('cls')
        API_KEY = 'kBtOz67nfvQq8t8HN6fA'
        ip_input = str(input(f'{color_6}IP{color_2}>'))
        req = requests.get(f'https://extreme-ip-lookup.com/json/{ip_input}?key={API_KEY}')
        req_json = req.json()
        sleep(0.5)
        pprint.pprint(req_json)
        returnf()
    except KeyboardInterrupt:
        print('Program interrupted')


def ping():
    try:
        sleep(0.5)
        os.system('cls')
        hostname = input(f'{color_6}Host{color_2}> ')
        response = os.system(f'ping {hostname}')
        if response == 0:
            print(f'{color_5}Status: {color_4}Online')
        else:
            print(f'{color_5}Status: {color_2}Offline')
        returnf()
    except KeyboardInterrupt:
        print('Program interrupted')


def pwgen():
    try:
        sleep(0.5)
        os.system('cls')
        passw = pwgenerator.generate()
        sleep(0.5)
        print(f'{color_5}password: {color_4}{passw}')
        returnf()
    except KeyboardInterrupt:
        print('Program interrupted')


def faken():
    try:
        sleep(0.5)
        os.system('cls')
        fake = Faker()
        name = fake.name()
        sleep(0.5)
        print(f'{color_5}fake name: {color_4}{name}')
        returnf()
    except KeyboardInterrupt:
        print('Program interrupted')


def fakeaddr():
    try:
        sleep(0.5)
        os.system('cls')
        fake = Faker()
        addr = fake.address()
        print(f'{color_5}fake address: {color_4}{addr}')
        returnf()
    except KeyboardInterrupt:
        print('Program interrupted')


def speedt():
    sleep(0.5)
    os.system('cls')
    os.system('speedtest --secure')
    returnf()


def dmlookup():

    domain = input(f'{color_6}domain{color_2}>')
    sleep(0.5)
    os.system('cls')
    os.system(f'nslookup {domain}')
    returnf()


def flushdns():
    sleep(0.5)
    os.system('cls')
    os.system('ipconfig /flushdns')
    returnf()


def portscan():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input(f'{color_6}IP{color_2}> ')
    range_port = int(input(f'{color_6}Range{color_2}> '))
    for ports in range(range_port):
        connect = s.connect_ex((host, ports))
        if connect == 0:
            print(f'{color_5}Port: {color_4}{ports} opened')
            s.close()
        else:
            print(f'{color_5}Port: {color_2}{ports} closed')
            s.close()
    returnf()


def tracing():
    host = input(f'{color_6}Host{color_2}>')
    sleep(0.5)
    os.system('cls')
    os.system(f'tracert {host}')
    returnf()


def backupf():
    archive = input(f'{color_6}Archive/folder path{color_2}>')
    new_path = input(f'{color_6}Backup path{color_2}>')
    sleep(0.5)
    os.system('cls')
    os.system(f'robocopy {archive} {new_path}')
    returnf()


def exitl():
    os.system('cls')
    confirm = input(
        f'{color_5}Are you sure you want to leave? [{color_4}Y{color_5}/{color_2}N{color_5}]>'
    ).strip().upper()

    if confirm == 'Y':
        print(f'{color_5}departure time:{color_4}{clock}')
        sleep(2)
        os.system('cls')
        sys.exit()
    else:
        os.system('cls')
        main()


def logo_installer():
    os.system('cls')
    logo_inst = f"""
    {color_1}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
            {color_6}██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗     ███████╗██████╗ 
            {color_6}██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     ██╔════╝██╔══██╗
            {color_6}██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     █████╗  ██████╔╝
            {color_6}██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     ██╔══╝  ██╔══██╗
            {color_6}██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗███████╗██║  ██║
            {color_6}╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
    {color_1}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    """
    print(logo_inst)


def installer():
    menu_installer = f"""
    {color_2}[1]  {color_6}OpenVPN               {color_2}[7]  {color_6}Steam
    {color_2}[2]  {color_6}VSCodium              {color_2}[8]  {color_6}Hyper terminal
    {color_2}[3]  {color_6}Google Chrome         {color_2}[9]  {color_6}Wireshark
    {color_2}[4]  {color_6}OperaGX               {color_2}[10] {color_6}Whatsapp
    {color_2}[5]  {color_6}Visual Studio Code    {color_2}[11] {color_6}VMware Player
    {color_2}[6]  {color_6}Discord               {color_2}[12] {color_6}VLC media player
    
    
    {color_5}V1.3 | {color_5}Entry time: {color_4}{clock} {color_5} | [{color_4}0{color_5}]{color_6}Return
    """
    print(menu_installer)


def openvpn():
    os.system('winget install openvpn')


def vscodium():
    os.system('winget install -e --id VSCodium.VSCodium')


def chrome():
    os.system('winget install -e --id Google.Chrome')


def operagx():
    os.system('winget install -e --id Opera.OperaGX')


def vscode():
    os.system('winget install -e --id Microsoft.VisualStudioCode')


def discord():
    os.system('winget install -e --id Discord.Discord')


def steam():
    os.system('winget install -e --id Valve.Steam')


def hyper():
    os.system('winget install -e --id Zeit.Hyper')


def wireshark():
    os.system('winget install -e --id WiresharkFoundation.Wireshark')


def whatsapp():
    os.system('winget install -e --id WhatsApp.WhatsApp')


def vmware():
    os.system('winget install -e --id VMware.WorkstationPlayer')


def vlc():
    os.system('winget install -e --id VideoLAN.VLC')


def main():
    try:
        if user_input == user and password_input == password:
            logo()
            menu()
            choice = int(input(f'{color_2}({color_6}root@root{color_2}){color_2}> '))
            while 1:
                match choice:
                    case 1:
                        req_ip()
                    case 2:
                        ping()
                    case 3:
                        pwgen()
                    case 4:
                        faken()
                    case 5:
                        fakeaddr()
                    case 6:
                        speedt()
                    case 7:
                        dmlookup()
                    case 8:
                        flushdns()
                    case 9:
                        portscan()
                    case 10:
                        tracing()
                    case 11:
                        backupf()
                    case 12:
                        sleep(0.5)
                        logo_installer()
                        installer()
                        choice_installer = int(input(f'{color_2}({color_6}root@root{color_2}){color_2}> '))
                        match choice_installer:
                            case 1:
                                openvpn()
                            case 2:
                                vscodium()
                            case 3:
                                chrome()
                            case 4:
                                operagx()
                            case 5:
                                vscode()
                            case 6:
                                discord()
                            case 7:
                                steam()
                            case 8:
                                hyper()
                            case 9:
                                wireshark()
                            case 10:
                                whatsapp()
                            case 11:
                                vmware()
                            case 12:
                                vlc()
                            case 0:
                                os.system('cls')
                                main()
                            case _:
                                otheroption()
                    case 0:
                        exitl()
                    case _:
                        otheroption()
        else:
            print(f'{color_2} User or Password is invalid!')
    except KeyboardInterrupt:
        print('Program interrupted')


main()
