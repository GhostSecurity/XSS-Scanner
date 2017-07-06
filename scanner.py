# XSS Scanner
import requests
from datetime import datetime
import os
import httplib
import colorama
import time
import urllib2
import sys
from termcolor import colored
from colorama import Fore, Back, Style
colorama.init()

def check_for_update():
    admin_github_url = "https://github.com/HydraBoy/XSS-Scanner"
    keyword = "ADMIN_FINDER_VERSION = '"
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
            os.popen("git pull "+ admin_github_url)
            print '[+] XSS Scanner Updated To Version: ' + content
            updated = True
    except Exception as ex:
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


def XSSFind(path=None,url):
  try:
    urls_path = open(path).readlines()
    
    # For Loop For Read Lines
    
    for link in urls_path:
      if '=' not in link:
        print(Fore.YELLOW+"[%s] [ERROR] URL [%s]" % (datatime.now(), link))
      else:
           _GET = urllib2.urlopen(link+'"<b>Ghost Security</b>',data=None)
           content = http.read()
           if 'Ghost Security' in content:
              print(Fore.RED+"[%s] [XSS] URL [%s]" % (datatime.now(), link))
              raw_input(Fore.GREEN+"[%s] [CONTINUE] [PRESS ENTER TO CONTINUE]" % (datatime.now()))
           else:
              print(Fore.GREEN+"[%s] [NEXT] URL [%s]" % (datatime.now(), link))
              
    raw_input(Fore.YELLOW+"[%s] [EXIT] [PRESS ENTER TO EXIT]" % (datatime.now()))
    


           
      
  
