#!/usr/bin/python

import sys, os, time
target = str(sys.argv[1])

def http_scan_http(http_port):
	cmd200 = 'nikto -host ' + target + ' -port ' + http_port + ' -evasion 5 2>&1 | tee http_scan.txt'
	cmd201 = 'whatweb --color=never --no-errors -a 3 -v http://' + target + http_port + ' 2>&1 | tee whatweb.txt'
	cmd202 = 'wapiti -u http://' + target + http_port + "/"
	print('[+] Running Nikto Scan... ')
	os.system(cmd200)
	print('[+] Running What Web Scan... ')
	os.system(cmd201)
	print('[+] Running Wapiti Scan... ')
	os.system(cmd202)

def http_scan_https(https_port):
	cmd250 = 'nikto -host ' + target + ' -port ' + https_port + ' -evasion 5 2>&1 | tee http_scan.txt'
	cmd251 = 'whatweb --color=never --no-errors -a 3 -v https://' + target + https_port + ' 2>&1 | tee whatweb.txt'
	cmd252 = 'wapiti -u http://' + target + https_port + "/"
	cmd253 = 'sslscan --show-certificate --no-colour' + target + https_port + ' 2>&1 | tee ssl-scan.txt'
	print('[+] Running Nikto Scan... ')
	os.system(cmd250)
	print('[+] Running What Web Scan... ')
	os.system(cmd251)
	print('[+] Running Wapiti Scan... ')
	os.system(cmd252)
	print('[+] Running SSL Scan... ')
	os.system(cmd253)
