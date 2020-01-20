#!/usr/bin/python

import sys, os, time
target = str(sys.argv[1])

def nikto_http(http_port):
	cmd4 = 'nikto -host ' + target + ' -port ' + http_port + ' -evasion 5 |tee nikto.txt'
	os.system(cmd4)

def nikto_https(https_port):
	cmd5 = 'nikto -host ' + target + ' -port ' + https_port + ' -evasion 5 |tee nikto.txt'
	os.system(cmd5)

