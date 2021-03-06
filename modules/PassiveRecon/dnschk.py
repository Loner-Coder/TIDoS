#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author : @_tID
#This module requires TIDoS Framework
#https://github.com/the-Infected-Drake/TIDoS-Framework 

import re
import time
import os
import sys
from colors import *
sys.path.append('files/')
from DNSDumpsterAPI import *

def dnschk(domain):

    print R+'\n   ====================='
    print R+'    D N S   L 0 0 K U P'
    print R+'   =====================\n'

    if 'http://' in domain:
	domain = domain.replace('http://','')
    elif 'https://' in domain:
	domain = domain.replace('https://','')
    else:
	pass

    res = DNSDumpsterAPI(False).search(domain)
    print(G+'\n [+] DNS Records')
    for entry in res['dns_records']['dns']:
        print(''+O+("{domain} ({ip}) {as} {provider} {country}".format(**entry)))
    for entry in res['dns_records']['mx']:
        print(G+"\n [+] MX Records")
        print(''+O+("{domain} ({ip}) {as} {provider} {country}".format(**entry)))
    print(G+"\n [+] Host Records (A)")
    for entry in res['dns_records']['host']:
        if entry['reverse_dns']:
            print(
                (''+O+"{domain} ({reverse_dns}) ({ip}) {as} {provider} {country}".format(**entry)))
        else:
            print(''+O+("{domain} ({ip}) {as} {provider} {country}".format(**entry)))
    print(G+'\n [+] TXT Records:')
    for entry in res['dns_records']['txt']:
        print(''+O+entry)
    print GR+' [*] Preparing DNS Map...'
    time.sleep(0.5)
    url = 'https://dnsdumpster.com/static/map/' + str(domain) + '.png'
    print GR+' [!] Fetching map...'
    try:
	os.system('wget -q ' + url)
    except:
	print R+' [-] Map generation failed!'
	sys.exit(1)
    st = str(domain) + '.png'
    st1 = str(domain)+'-dnsmap.jpg'
    p = 'mv '+st+' '+ st1
    os.system(p)
    mov = 'mv '+ st1 + ' files/'
    os.system(mov)
    print G+' [+] Map saved under "files/' + st1 + '"'
    try:
        print GR+' [!] Trying to open DNS Map...'
        os.system('xdg-open files/'+st1)
    except:
	print R+' [-] Failed to open automatically.'
	print GR+' [!] Please view the map manually.' 

