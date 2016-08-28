#!/usr/bin/python

##
#
# A naive graphical interpretation of the "df -h" command
# It grabs the primary dev filesystems (usually main disks) using grep
#
# Author: Willie Stevenson
#
##

import subprocess
import re

# draws the graphical representation - drawing is approximately accurate
def draw(used_space):
	print
	print "[",
	print u"\u2588" * used_space,
	print ' ' * (100 - used_space),
	print "]"

def main():
	output = subprocess.check_output("df -h | grep /dev/", shell=True)

	for line in output.splitlines():

		arr = line.split()

		used_space = numbers_used_size = re.sub(r'\D', '', arr[4])

		draw(int(used_space))

		print "[Filesystem:", arr[0], "  ", "Total Space:", arr[1], "  ", "Used Space:", arr[2], " ", "Percent Used:", arr[4], " ", "Mounted On:", arr[-1], " ", "]"  
		print
		
if __name__ == "__main__":
	main()