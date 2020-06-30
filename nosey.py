#!/usr/bin/python

import sys, os, time
import http_scan
import dirb
# import bforce
import smb
import other_svc


if len(sys.argv) > 1:
    target = str(sys.argv[1])
else:
    print('Please Provide A Target To Scan [ Ex: python ./nosey.py 10.10.1.10 ]')



'''
cmd 100+ = dirb
cmd 200+ = http
cmd 300+ = adv_http
cmd 400+ = dns
cmd 500+ = bforce
cmd 600+ = smb
cmd 700+ = other_svc

Nosey Neighbor, is a simple automated python script linux based tools to complete basic pen test enumeration
Ex: python ./nosey.py 10.10.1.10
'''
# Bling section:

green = 'echo "\e[32m"'
red = 'echo "\e[31m"'
yellow = 'echo "\e[33m"'
plain = 'echo "\e[0m"'


os.system(yellow)

print ('''
8b,dPPYba,    ,adPPYba,   ,adPPYba,   ,adPPYba,  8b       d8  
88P'   `"8a  a8"     "8a  I8[    ""  a8P_____88  `8b     d8'  
88       88  8b       d8   `"Y8ba,   8PP"""""""   `8b   d8'   
88       88  "8a,   ,a8"  aa    ]8I  "8b,   ,aa    `8b,d8'    
88       88   `"YbbdP"'   `"YbbdP"'   `"Ybbd8"'      Y88'     
            ._   _  o  _  |_  |_   _  ._             d8'      
            | | (/_ | (_| | | |_) (_) |             d8'       
                       _|               
-----------------------------------------------------------
#                                Sniffing @ Your Network  #
-----------------------------------------------------------
''')

os.system(plain)

def nmap():
	cmd = 'nmap -vv --reason -Pn -A --osscan-guess --version-all -p- ' + target + ' -oA nosey-scan '
	cmd2 = 'nmap -sU -T4 -p1-1000 -sC -sV ' + target + ' -oA nosey-udp-scan '
	os.system(green)
	print('[+] Command run: ' + cmd)
	os.system(plain)
	os.system(cmd)
	os.system(cmd2)
		
nmap()
print('\n')
print('-\/-' * 15)
print(' ')
os.system(green)
print('[+] Nmap completed...')
print(' ')
os.system(plain)
print('[+] Checking for open ports')
time.sleep(3)
print(' ')

http = os.system('cat nosey-scan.nmap | grep --color -E "(^|\s)http($|\s)"')
http_port = str(os.system("cat nosey-scan.nmap | grep --color -E '(^|\s)http($|\s)' | awk -F/ '{print $1}' "))
https = os.system('cat nosey-scan.nmap | grep --color -E "(^|\s)https($|\s)"')
https_port = str(os.system("cat nosey-scan.nmap | grep --color -E '(^|\s)https($|\s)' | awk -F/ '{print $1}' "))
smb0 = os.system('cat nosey-scan.nmap | grep --color -E "(^|\s)msrpc($|\s)"')
smb0_port = str(os.system("cat nosey-scan.nmap | grep --color -E '(^|\s)msrpc($|\s)' | awk -F/ '{print $1}' "))
smb1 = os.system('cat nosey-scan.nmap | grep --color -E "(^|\s)netbios($|\s)"')
smb1_port = str(os.system("cat nosey-scan.nmap | grep --color -E '(^|\s)netbios($|\s)' | awk -F/ '{print $1}' "))
smb2 = os.system('cat nosey-scan.nmap | grep --color -E "(^|\s)microsoft-ds($|\s)"')
smb2_port = str(os.system("cat nosey-scan.nmap | grep --color -E '(^|\s)microsoft-ds($|\s)' | awk -F/ '{print $1}' "))
ssh = os.system('cat nosey-scan.nmap | grep --color -E "(^|\s)ssh($|\s)"')
ssh_port = str(os.system("cat nosey-scan.nmap | grep --color -E '(^|\s)ssh($|\s)' | awk -F/ '{print $1}' "))
snmp = os.system('cat nosey-udp-scan.nmap | grep --color -E "(^|\s)snmp($|\s)"')
snmp_port = str(os.system("cat nosey-udp-scan.nmap | grep --color -E '(^|\s)snmp($|\s)' | awk -F/ '{print $1}' "))
dns = os.system('cat nosey-udp-scan.nmap | grep --color -E "(^|\s)dns($|\s)"')
dns_port = str(os.system("cat nosey-udp-scan.nmap | grep --color -E '(^|\s)dns($|\s)' | awk -F/ '{print $1}' "))
isa = os.system('cat nosey-udp-scan.nmap | grep --color -E "(^|\s)isa($|\s)"')
isa_port = str(os.system("cat nosey-udp-scan.nmap | grep --color -E '(^|\s)isa($|\s)' | awk -F/ '{print $1}' "))
nfs = os.system('cat nosey-udp-scan.nmap | grep --color -E "(^|\s)nfs($|\s)"')
nfs_port = str(os.system("cat nosey-udp-scan.nmap | grep --color -E '(^|\s)nfs($|\s)' | awk -F/ '{print $1}' "))


print(' ')
print('-\/-' * 15)
print(' ')

# Change to a master function to replace multiple ifs...

if http == 0:
	os.system(green)
	print('[+] Starting HTTP Directory Scans...\n')
	os.system(plain)
	dirb.dirb_http(http_port)
	print('\n')
	print('-\/-' * 15)
	print('\n')
	os.system(green)
	print('[+] Starting HTTP Service Scans...\n')
	os.system(plain)
	http_scan.http_scan_http(http_port)

elif https == 0:
	os.system(green)
	print('[+] Starting HTTPS Directory Scans...\n')
	os.system(plain)
	dirb.dirb_https(https_port)
	print('\n')
	print('-\/-' * 15)
	print('\n')
	os.system(green)
	print('[+] Starting HTTPS Service Scans...\n')
	os.system(plain)
	http_scan.http_scan_https(https_port)
	
else:
	os.system(red)
	print('No HTTP/S ports found on standard numbering, check Nmap results to make sure.')
	os.system(plain)

# If tcp 135,139, or 445 is open

if smb0 == 0:
	os.system(green)
	print('[+] Starting SMB / Samba service scan...\n')
	os.system(plain)
	smb.smb_windows_rpc(smb0_port)
	print('\n')
	print('-\/-' * 15)
	print('\n')
elif smb1 == 0:
	os.system(green)
	print('[+] Starting SMB / Samba service scan...\n')
	os.system(plain)
	smb.smb_windows_share(smb1_port)
	print('\n')
	print('-\/-' * 15)
	print('\n')
elif smb2 == 0:
	os.system(green)
	print '[+] Starting SMB / Samba service scan...\n'
	os.system(plain)
	smb.smb_windows_domain(smb2_port)
	print('\n')
	print('-\/-' * 15)
	print('\n')
else:
	os.system(red)
	print 'No open SMB ports found on standard numbering, check Nmap results to make sure.'
	os.system(plain)

# If any un-common network services are open

if ssh == 0:
	os.system(green)
	print('[+] Starting SSH service scan...\n')
	os.system(plain)
	other_svc.ssh_svc(ssh_port)
#	bforce.bforce_ssh()
	print('\n')
	print('-\/-' * 15)
	print('\n')
elif snmp == 0:
	os.system(green)
	print('[+] Starting SNMP service scan...\n')
	os.system(plain)
	other_svc.snmp_svc(snmp_port)
	print('\n')
	print('-\/-' * 15)
	print('\n')
elif dns == 0:
	os.system(green)
	print('[+] Starting DNS service scan...\n')
	os.system(plain)
	other_svc.dns_svc(dns_port)
	print('\n')
	print('-\/-' * 15)
	print('\n')
elif isa == 0:
	os.system(green)
	print('[+] Starting ISA service scan...\n')
	os.system(plain)
	other_svc.isa_svc(isa_port)
	print('\n')
	print('-\/-' * 15)
	print('\n')
elif nfs == 0:
	os.system(green)
	print('[+] Starting NFS service scan...\n')
	os.system(plain)
	other_svc.nfs_svc(nfs_port)
	print('\n')
	print('-\/-' * 15)
	print('\n')
else:
	os.system(red)
	print 'No uncommon service ports found.'
	os.system(plain)

os.system(green)
print '[+] Listing scan results ...'
os.system(plain)

os.system('ls -la')
exit(0)
