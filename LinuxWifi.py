#!/usr/bin/env python3

#importing module named subprocess
import subprocess

#getting user input to ask wifi ssid
ssid = input("enter ssid:\n")

#running the command to show password for the given wifi ssid
subprocess.run("cd /etc/NetworkManager/system-connections/ && sudo cat " + ssid + " | grep 'psk='" , shell=True)