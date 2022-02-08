#!/usr/bin/env python3

#importing sys module
import sys

#importing module named subprocess
import subprocess

def my_except_hook(exctype, value, traceback):
        print('Usage: python3', args[0] + ' <SSID>')
sys.excepthook = my_except_hook

#The sys module in Python has the argv functionality. This functionality returns a list of all command-line arguments provided to the python file when triggering an execution of it through terminal.
args = sys.argv

#ACII art
a = '''
 +-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+
 |c|o|d|e| |b|y| |m|a|n|s|o|o|r|.|c|o|d|e|
 +-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+
'''
print(a)

 #running the command to show password for the given wifi ssid
subprocess.run("cd /etc/NetworkManager/system-connections/ && sudo cat " + args[1] + " | grep 'psk=' | awk '{print substr($1,5)}'" , shell=True)