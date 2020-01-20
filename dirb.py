#!/usr/bin/python

import sys, os, time
target = str(sys.argv[1])

def dirb_http(http_port):
	cmd2 = 'dirb http://' + target + ':' + http_port + ' -r |tee dirb_http.txt'
	os.system(cmd2)

def dirb_https(https_port):
	cmd3 = 'dirb https://' + target + ':' + https_port + ' -r |tee dirb_https.txt'
	os.system(cmd3)

