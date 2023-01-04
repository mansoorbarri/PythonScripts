#!/usr/bin/env python3

# import needed libraries
import sys
import subprocess

# set variables
args = sys.argv
beta_dir = "~/Music/anar/hugo/beta.mansoorbarri.com/"
base_dir = "~/Music/anar/hugo/mansoorbarri.com/"
x=" "
post_md = args[2] + ".md"

# copy the images 
subprocess.run("cp -r " + beta_dir + "images/" + args[1] + args[2] + x + base_dir + "images/" + args[1] + args[2], shell=True)

print("\n Images copied to: " + base_dir + "images/" + args[1] + args[2])

# copy .md file
subprocess.run("cp -r " + beta_dir + "content/" + args[1] + post_md + x + base_dir + "content/" + args[1], shell=True)

print("\n .md file copied to: " + base_dir + "content/" + args[1] + args[2])

# delete the files
subprocess.run("rm -rf " + beta_dir + "images/" + args[1] + args[2] + "/*", shell=True)

subprocess.run("rm -rf " + base_dir + "images/" + args[1] + args[2] + "/*", shell=True)

exit()