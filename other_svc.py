#!/usr/bin/python

import sys, os, time
target = str(sys.argv[1])

def ssh_svc(ssh_port):
    cmd700 = 'sslscan --show-certificate --no-colour ' + target + ':' + ssh_port + ' 2>&1 | tee -a ssl-scan.txt'
    cmd701 = 'nmap -vv --reason -Pn -sV -p ' + ssh_port + ' --script="banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods" -oA nosey-ssh-scan ' + target
    os.system(cmd700)
    os.system(cmd701)

def snmp_svc(snmp_port):
    cmd710 = 'snmp-check -t '+ target + ' -c public 2>&1 | tee -a snmp-scan.txt'
    cmd711 = 'snmpwalk -v2 c -c public ' + target + '2>&1 | tee -a snmp-scan.txt'
    cmd712 = 'snmp-check -t '+ target + ' -c private 2>&1 | tee -a snmp-scan.txt'
    cmd713 = 'snmpwalk -v2 c -c private ' + target + '2>&1 | tee -a snmp-scan.txt'
    cmd714 = 'snmp-check -t '+ target + ' -c community 2>&1 | tee -a snmp-scan.txt'
    cmd715 = 'snmpwalk -v2 c -c community ' + target + '2>&1 | tee -a snmp-scan.txt'
    os.system(cmd710)
    os.system(cmd711)
    os.system(cmd712)
    os.system(cmd713)
    os.system(cmd714)
    os.system(cmd715)

def dns_svc(dns_port):
    cmd720 = 'dig axfr domain.name @' + target + ' 2>&1 | tee -a dns-transfer.txt'
    os.system(cmd720)

def isa_svc(isa_port): ## If this fails the tool may need to be installed ex: apt install ike-scan
    cmd730 = 'ike-scan ' + target + ' 2>&1 | tee -a isa-scan.txt'
    os.system(cmd730)

def nfs_svc(nfs_port):
    cmd740 = 'showmount -e ' + target + ' 2>&1 | tee -a nfs-scan.txt'
    os.system(cmd740)

