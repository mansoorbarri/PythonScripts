#!/usr/bin/env python3

a = '''
 +-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+
 |c|o|d|e| |b|y| |m|a|n|s|o|o|r|.|c|o|d|e|
 +-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+
'''
print(a)

#importing module named subprocess
import subprocess

#getting user input to ask wifi ssid
ssid = input("enter ssid:\n")

#running the command to show password for the given wifi ssid
subprocess.run("cd /etc/NetworkManager/system-connections/ && sudo cat " + ssid + " | grep 'psk=' | awk '{print substr($1,5)}'" , shell=True)
