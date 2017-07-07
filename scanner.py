# XSS Scanner 
# Created By Ghost Security Team

import requests
from time import gmtime, strftime
import os
import subprocess
import httplib
import colorama
import time
import urllib2
import urllib
import platform
import sys
from termcolor import colored
from colorama import Fore, Back, Style
colorama.init()

def clear():
    if platform.system() == 'Windows':
        os.popen("cls")
    else:
        subprocess.call("clear",shell=True)

def Welcome():
    print (Fore.GREEN+"""
    ################################
    #                              #
    #         XSS Scanner          #
    #                              #
    #     Ghost Security Team      #
    #                              #
    ################################
    """)

def check_for_update():
    admin_github_url = "https://github.com/HydraBoy/XSS-Scanner"
    updated = False
    print(Fore.GREEN+"[{}] [UPDATE] 'Checking For Updates And Debuging...'".format(strftime("%H:%M:%S", gmtime())))
    time.sleep(1)
    try:
        http = urllib2.urlopen('https://raw.githubusercontent.com/HydraBoy/XSS-Scanner/master/.version.txt',data=None)
        content = http.read()
        scan = urllib2.urlopen('https://raw.githubusercontent.com/HydraBoy/XSS-Scanner/master/scanner.py',data=None)
        reader = scan.read()
        scanner = open('scanner.py','r').read()
        read = open('.version.txt','r').read()
        if read == content:
            print(Fore.GREEN+"[{}] [UP-TO-DATA] 'No available updates...'".format(strftime("%H:%M:%S", gmtime())))
            if scanner != reader:
                print(Fore.GREEN+"[{}] [DEBUG] 'Debuging Detected...'".format(strftime("%H:%M:%S", gmtime())))
                time.sleep(1)
                print(Fore.GREEN+"[{}] [DEBUG] 'Debuging XSS-Scanner Tool...'".format(strftime("%H:%M:%S", gmtime())))
                os.popen('rm -rf scanner.py')
                urllib.urlretrieve("https://raw.githubusercontent.com/HydraBoy/XSS-Scanner/master/scanner.py","scanner.py")
                print(Fore.GREEN+"[{}] [DEBUG] 'Debug Complated'".format(strftime("%H:%M:%S", gmtime())))
                sys.exit(Fore.GREEN+"[{}] [RELAUNCH] 'Plase Relaunch The Script.'".format(strftime("%H:%M:%S", gmtime())))
        else:
            print(Fore.GREEN+"[{}] [UPDATE] 'Updating XSS-Scanner Tool...'".format(strftime("%H:%M:%S", gmtime())))
            os.popen('rm -rf .version.txt;rm -rf scanner.py')
            urllib.urlretrieve("https://raw.githubusercontent.com/HydraBoy/XSS-Scanner/master/scanner.py","scanner.py")
            urllib.urlretrieve("https://raw.githubusercontent.com/HydraBoy/XSS-Scanner/master/.version.txt",".version.txt")
            print(Fore.GREEN+"[{}] [UPDATED] XSS Scanner Updated To Version: ".format(strftime("%H:%M:%S", gmtime())))
            updated = True
    except Exception as ex:
        print ex
        print "\n[!] Problem while updating."
    if updated:
        sys.exit(Fore.GREEN+"[{}] [RELAUNCH] 'Plase Relaunch The Script.'".format(strftime("%H:%M:%S", gmtime())))


# Check If URL in available URL.


def IsUrl(url):
    if 'https://' not in str(url):
        if 'http://' in str(url):
            XSSFind(url)
        else:

            XSSFind("http://" + str(url))
    else:
        if 'http://' not in str(url):
            if 'https://' in str(url):
                XSSFind(url)
            else:
                XSSFind("http://" + str(url))


# XSS Scanner. Check If Target URL has XSS Bug.


def XSSFind(path):
    try:
        urls_path = open(path).readlines()

        # For Loop For Read Lines
        if open(path).read() == "":
            print(Fore.YELLOW+"[{}] [ERROR] 'EMPETY TXT FILE'".format(strftime("%H:%M:%S", gmtime())))
        else:
            print(Fore.GREEN+"[{}] [STARTED] 'Scanning...'".format(strftime("%H:%M:%S", gmtime())))
            for links in urls_path:
                link = links.replace("\n","")
                if '=' not in link:
                    print(Fore.YELLOW+"[{}] [ERROR] URL [{}]".format(strftime("%H:%M:%S", gmtime()), link))
                else:
                    _GET = urllib2.urlopen('%s"<b>ghostsec</b>' % (link))
                    content = _GET.read()
                    if 'ghostsec' in str(content) or '"ghostsec' in str(content):
                        print(Fore.RED+"[{}] [XSS] URL [{}]".format(strftime("%H:%M:%S", gmtime()), link))
                    else:
                        print(Fore.GREEN+"[{}] [NEXT] URL [{}] ".format(strftime("%H:%M:%S", gmtime()), link))
                        
            print(Fore.GREEN+"[{}] [DONE] 'All URLs Scanned..'".format(strftime("%H:%M:%S", gmtime())))
            raw_input(Fore.YELLOW+"[{}] [RETRY] [ALL URLS SCANNED PRESS ENTER TO RETRY]".format(strftime("%H:%M:%S", gmtime())))

    except Exception as err:
        print err

clear()
Welcome()
check_for_update()
while 1:
    try:
        urls = raw_input(Fore.RED+"[{}] [INPUT] [ENTER FILE NAME]: ".format(strftime("%H:%M:%S", gmtime())))
        if urls == "":
            print(Fore.YELLOW+"[{}] [ERROR] 'PLASE ENTER TXT FILE NAME'".format(strftime("%H:%M:%S", gmtime())))
        elif open(urls).read() == "":
            print(Fore.YELLOW+"[{}] [ERROR] 'EMPETY TXT FILE'".format(strftime("%H:%M:%S", gmtime())))
        else:
            XSSFind(urls)
    except (KeyboardInterrupt, SystemExit):
        exit(Fore.YELLOW+"\n[{}] [GAME OVER] 'GOOD LUCK ;)'".format(strftime("%H:%M:%S", gmtime())))
    except IOError as err:
        if 'No such file or directory:' in str(err):
            print(Fore.YELLOW+"[{}] [ERROR] 'INVALID FILE NAME'".format(strftime("%H:%M:%S", gmtime())))
