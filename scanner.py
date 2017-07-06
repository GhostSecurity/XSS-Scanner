# XSS Scanner
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
        os.popen("clear").read()

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
    print "\n[*] Checking for XSS-Scanner updates.."
    time.sleep(1)
    try:
        http = urllib2.urlopen('https://raw.githubusercontent.com/HydraBoy/XSS-Scanner/master/.version.txt',data=None)
        content = http.read()
        read = open('.version.txt','r').read()
        if read == content:
            print '[#] No updates available.'
        else:
            print '[+] Updating XSS-Scanner Tool...'
            os.popen('rm -rf .version.txt')
            urllib.urlretrieve("https://raw.githubusercontent.com/HydraBoy/XSS-Scanner/master/.version.txt",".version.txt")
            print '[+] XSS Scanner Updated To Version: ' + content
            updated = True
    except Exception as ex:
        print ex
        print "\n[!] Problem while updating."
    if updated:
        sys.exit(Fore.GREEN+"[!] Plase Relaunch The Script.")


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
            print(Fore.GREEN+"\n[!] Started at [{}]".format(strftime("%H:%M:%S", gmtime())))
            for links in urls_path:
                link = links.replace("\n","")
                if '=' not in link:
                    print(Fore.YELLOW+"[{}] [ERROR] URL [{}]".format(strftime("%H:%M:%S", gmtime()), link))
                else:
                    _GET = urllib2.urlopen('{}"<b>Ghost Security</b>'.format(link))
                    content = _GET.read()
                    if 'Ghost Security' in content or '"' in content:
                        print(Fore.RED+"[{}] [XSS] URL [{}]".format(strftime("%H:%M:%S", gmtime()), link))
                    else:
                        print(Fore.GREEN+"[{}] [NEXT] URL [{}] ".format(strftime("%H:%M:%S", gmtime()), link))

            raw_input(Fore.YELLOW+"\n[{}] [RETRY] [PRESS ENTER TO RETRY]".format(strftime("%H:%M:%S", gmtime())))
            print(Fore.GREEN+"\n[!] Ended at [{}]".format(strftime("%H:%M:%S", gmtime())))

    except Exception as err:
        print err

clear()
Welcome()
check_for_update()
while 1:
    try:
        urls = raw_input(Fore.RED+"\nEnter URL(s) TXT file\n>>> ")
        if urls == "":
            print(Fore.YELLOW+"\n[{}] [ERROR] 'PLASE ENTER TXT FILE NAME'".format(strftime("%H:%M:%S", gmtime())))
        elif open(urls).read() == "":
            print(Fore.YELLOW+"\n[{}] [ERROR] 'EMPETY TXT FILE'".format(strftime("%H:%M:%S", gmtime())))
        else:
            XSSFind(urls)
    except (KeyboardInterrupt, SystemExit):
        exit(Fore.YELLOW+"\n\n[{}] [GAME OVER] 'GOOD LUCK ;)'\n".format(strftime("%H:%M:%S", gmtime())))
    except IOError as err:
        if 'No such file or directory:' in str(err):
            print(Fore.YELLOW+"\n\n[{}] [ERROR] 'INVALID FILE NAME'".format(strftime("%H:%M:%S", gmtime())))
