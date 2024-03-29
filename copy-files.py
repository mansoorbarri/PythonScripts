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
subprocess.run("cp -r " + beta_dir + "images/" + args[1] + args[2] + x + "~/Documents/GitHub/website/" + "images/" + args[1] + args[2], shell=True)

print("\n Images copied to: " + base_dir + "images/" + args[1] + args[2])

# copy .md file
subprocess.run("cp -r " + beta_dir + "content/" + args[1] + post_md + x + base_dir + "content/" + args[1], shell=True)

print("\n .md file copied to: " + base_dir + "content/" + args[1] + args[2])

# delete the files
subprocess.run("rm -rf " + beta_dir + "images/" + args[1] + args[2] + "/*", shell=True)
print("\n Files deleted")

# commit + push
subprocess.run("cd ~/Documents/GitHub/website/ &&  ~/git add . && git commit -m 'new post' && git push", shell=True)

# print url 
print("\n post live at: https://mansoorbarri.com/" + args[1] + args[2])

# edit + push README
my_file = open("/home/anar/Documents/GitHub/mansoorbarri/README.md")
string_list = my_file.readlines()

my_file.close()

title = input("title: ")
string_list[9] = "\n- [" + title + "](mansoorbarri.com/" + args[1] + args[2] + ")\n"

del string_list[12]

my_file = open("/home/anar/Documents/GitHub/mansoorbarri/README.md", "w")
new_file_contents = "".join(string_list)

my_file.write(new_file_contents)
my_file.close()

subprocess.run("git add . && git commit -m 'updated' && git push", shell=True)
print("\n README edited and pushed")

exit()