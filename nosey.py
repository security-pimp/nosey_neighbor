#!/usr/bin/python

import sys, os, time
import nikto
import dirb
import smb

target = str(sys.argv[1])

'''
cmd 2,3 = dirb
cmd 4,5 = nikto
cmd 6 = smb
Nosey Neighbour, simple automated python script using bash to complete simple enum scripts

For now runs broad nmap, dirb, nikto, smb. Modify the commands in each file to get a different result.
Still a work in progress, figuring it out.
ASCII ART: http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
Eg: python ./nosey.py 10.10.1.10

'''
# Bling section:

green = 'echo "\e[32m"'
red = 'echo "\e[31m"'
yellow = 'echo "\e[33m"'
plain = 'echo "\e[0m"'


os.system(yellow)

print '''
  _   _                        _   _      _       _     _                       
 | \ | | ___  ___  ___ _   _  | \ | | ___(_) __ _| |__ | |__   ___  _   _ _ __  
 |  \| |/ _ \/ __|/ _ \ | | | |  \| |/ _ \ |/ _` | '_ \| '_ \ / _ \| | | | '__| 
 | |\  | (_) \__ \  __/ |_| | | |\  |  __/ | (_| | | | | |_) | (_) | |_| | |    
 |_| \_|\___/|___/\___|\__, | |_| \_|\___|_|\__, |_| |_|_.__/ \___/ \__,_|_|    
                       |___/                |___/                               

stickfish V1.1 2019

'''

os.system(plain)

def nmap():
	cmd = 'nmap -vv --reason -Pn -A --osscan-guess --version-all -p- ' + target + ' -oA nosey-scan '
	os.system(green)
	print '[+] Command run: ' + cmd
	os.system(plain)
	os.system(cmd)
		
nmap()
print '\n'
print '-\/-' * 15
print ' '
os.system(green)
print '[+] Nmap completed...'
print ' '
os.system(plain)
print '[+] Checking for open ports'
time.sleep(3)
print ' '

http = os.system('cat nosey-scan.nmap | grep --color -E "(^|\s)http($|\s)"')
http_port = os.system("cat nosey-scan.nmap | grep --color -E '(^|\s)http($|\s)' | awk -F/ '{print $1}' ")
https = os.system('cat nosey-scan.nmap | grep --color -E "(^|\s)https($|\s)"')
https_port = os.system("cat nosey-scan.nmap | grep --color -E '(^|\s)https($|\s)' | awk -F/ '{print $1}' ")
smb0 = os.system('cat nosey-scan.nmap | grep --color -E "(^|\s)msrpc($|\s)"')
smb1 = os.system('cat nosey-scan.nmap | grep --color -E "(^|\s)netbios($|\s)"')
smb2 = os.system('cat nosey-scan.nmap | grep --color -E "(^|\s)microsoft-ds($|\s)"')
ssh = os.system('cat nosey-scan.nmap | grep --color -E "(^|\s)ssh($|\s)"')


# future = os.system('cat nosey-scan.nmap | grep --color 443/tcp')

print ' '
print '-\/-' * 15
print ' '

# Change to a master function to replace multiple ifs...

if http == 0:
	os.system(green)
	print '[+] Starting HTTP Directory Scans...\n'
	os.system(plain)
	dirb.dirb_http(http_port)
	print '\n'
	print '-\/-' * 15
	print '\n'
	os.system(green)
	print '[+] Starting HTTP Service Scans...\n'
	os.system(plain)
	nikto.nikto_http(http_port)

elif https == 0:
	os.system(green)
	print '[+] Starting HTTPS Directory Scans...\n'
	os.system(plain)
	dirb.dirb_https(https_port)
	print '\n'
	print '-\/-' * 15
	print '\n'
	os.system(green)
	print '[+] Starting HTTPS Service Scans...\n'
	os.system(plain)
	nikto.nikto_https(https_port)
	
else:
	os.system(red)
	print 'No HTTP/S ports found on standard numbering, check Nmap results to make sure.'
	os.system(plain)

# If tcp 445 open

if smb0 == 0:
	os.system(green)
	print '[+] Starting SMB / Samba service scan...\n'
	os.system(plain)
	smb.smb_windows_share()
	print '\n'
	print '-\/-' * 15
	print '\n'
elif smb1 == 0:
	os.system(green)
	print '[+] Starting SMB / Samba service scan...\n'
	os.system(plain)
	smb.smb_windows_domain()
	print '\n'
	print '-\/-' * 15
	print '\n'
elif smb2 == 0:
	os.system(green)
	print '[+] Starting SMB / Samba service scan...\n'
	os.system(plain)
	smb.smb_windows_rpc()
	print '\n'
	print '-\/-' * 15
	print '\n'	
else:
	os.system(red)
	print 'No open SMB ports found on standard numbering, check Nmap results to make sure.'
	os.system(plain)

os.system(green)
print '[+] Listing scan results ...'
os.system(plain)

os.system('ls -la')
exit(0)
