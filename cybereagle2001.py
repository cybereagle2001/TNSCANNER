#!/usr/bin/python3
#coded by cybereagle2001
#pip3 install python-nmap

"""
MIT License

Copyright (c) 2021 Oussama Ben Hadj Dahman

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import nmap 
import os
sc= nmap.PortScanner()
def banner():
    print(
"""  \033[0;32m                                                                                                        
MMP""MM""YMM `7MN.   `7MF'.MMMbgD   .g8''''bgd     db      `7MN.   `7MF'`7MN.   `7MF'`7MM|||YMM    MM||Mq.  
P'   MM   `7   MMN.    M ,MI    "Y .dP'     `M    ;MM:       MMN.    M    MMN.    M    MM    `7    MM   `MM. 
     MM        M YMb   M `MMb.     dM'       `   ,V^MM.      M YMb   M    M YMb   M    MM   d      MM   ,M9  
     MM        M  `MN. M   `YMMNq. MM           ,M  `MM      M  `MN. M    M  `MN. M    MMmmMM      MMmmdM9   
     MM        M   `MM.M .     `MM MM.          AbmmmqMA     M   `MM.M    M   `MM.M    MM   Y  ,   MM  YM.   
     MM        M     YMM Mb     dM `Mb.     ,' A'     VML    M     YMM    M     YMM    MM     ,M   MM   `Mb. 
   .JMML.    .JML.    YM P"Ybmmd"    `"bmmmd'.AMA.   .AMMA..JML.    YM  .JML.    YM  .JMMmmmmMMM .JMML. .JMM.

                                                                        \033[1;94m    by cybereagle2001\033[0m
                                                                                                             
""")

def menu():
    os.system('clear')
    banner()
    menu = int(input("choose your option: \n1- Network scanner \n2- Vulerability detection \n3- Exploitation\n\n\033[1;31muser$> \033[0m"))
    if (menu == 1):
        nmap()
    elif (menu ==2):
        vuln()
    elif (menu ==3):
        exploit()
    else:
        os.system('clear')
        menu()

def main():
    main_menu=int(input("choose your option: \n 1- Install\n 2- Run the Script\n\n user >> "))
    if (main_menu == 1):
        os.system('python3 install.py')
    else:
        menu()

def nmap():
    os.system("clear")
    print("""\033[1;92m
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                        SCAN FOR OPEN PORTS
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    \033[0m""")
    ip= input("What is the IP to scan: ")
    sc.scan(ip,'1-1024')
    for host in sc.all_hosts():
        print('\033[1;31m---------------------------------------------\033[0m')    
        print('Host :\033[0;32m %s (%s)\033[0m' % (host, sc[host].hostname()))
        print('State :\033[0;32m %s\033[0m' % sc[host].state())
        for proto in sc[host].all_protocols():
            print("\033[1;31m*******************\033[0m")
            print('Protocol : %s' % proto)

            lport= sc[host][proto].keys()
            for port in lport:
                print('port : \033[0;33m%s\t\033[0mstate :\033[0;33m %s\033[0m' % (port, sc[host][proto][port]['state']))

def vuln():
    os.system('clear')
    print("""\033[0;35m
        //////////////////////////////////////
               Vulnerability Detection
        /////////////////////////////////////\033[0m
    """)
    ip = input('what is the ip to scan: ')
    if  (";" in ip):
        ip = ip.split(";")
        os.system("cd vulscan && nmap -sV --script=vulscan.nse "+ip[0])
    elif("&&" in ip):
        ip = ip.split("&&")
        os.system("cd vulscan && nmap -sV --script=vulscan.nse "+ip[0])
    else:
        os.system("cd vulscan && nmap -sV --script=vulscan.nse "+ip)

def exploit():
    os.system("clear && msfconsole")

if __name__ == "__main__":
    main()