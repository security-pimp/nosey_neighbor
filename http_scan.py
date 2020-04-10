#!/usr/bin/python

import sys, os, time
target = str(sys.argv[1])

def http_scan_http(http_port):
	cmd200 = 'nikto -host ' + target + ' -port ' + http_port + ' -evasion 5 |tee http_scan.txt'
	cmd201 = 'whatweb --color=never --no-errors -a 3 -v http://' + target + http_port + ' |tee whatweb.txt'
	os.system(cmd200)
	os.system(cmd201)

def http_scan_https(https_port):
	cmd250 = 'nikto -host ' + target + ' -port ' + https_port + ' -evasion 5 |tee http_scan.txt'
	cmd251 = 'sslscan --show-certificate --no-colour' + target +  https_port + ' |tee ssl-scan.txt
	cmd252 = 'whatweb --color=never --no-errors -a 3 -v https://' + target + http_port + ' |tee whatweb.txt'
	os.system(cmd250)
	os.system(cmd251)
	os.system(cmd252)
