#!/usr/bin/python

import sys, os, time
target = str(sys.argv[1])

def dirb_http(http_port):
	cmd100 = 'dirb http://' + target + ':' + http_port + ' -r |tee dirb_http.txt'
	cmd101 = 'gobuster dir -u http://' + target + http_port + ' -w /usr/share/wordlists/dirb/common.txt -q -n -e | tee gobuster.txt
	cmd102 = 'eyewitness -f gobuster.txt -d eyewitness --web --no-prompt'
	os.system(cmd100)
	os.system(cmd101)
	os.system(cmd102)

def dirb_https(https_port):
	cmd150 = 'dirb https://' + target + ':' + https_port + ' -r |tee dirb_https.txt'
	cmd151 = 'gobuster dir -u https://' + target + https_port + ' -w /usr/share/wordlists/dirb/common.txt -q -n -e | tee gobuster.txt
	cmd152 = 'eyewitness -f gobuster.txt -d eyewitness --web --no-prompt'
	os.system(cmd150)
	os.system(cmd151)
	os.system(cmd152)

