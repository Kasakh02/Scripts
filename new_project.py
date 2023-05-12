import sys
import os
import shutil

if (len(sys.argv) == 3):
	main_folder = sys.argv[1]
else:
	print("Usage: new {project name} {number of exercises}")
	quit()

try:
	if ((sys.argv[2]).isdigit()):
		os.mkdir(main_folder)
		nbr_exs = (int)(sys.argv[2])
	else:
		print("{number of exercises} has to be a valid integer")
		quit()
except OSError:
	print("file " + '"' + main_folder + '"' + " already exists")
	quit()

for i in range(nbr_exs):
	os.mkdir(main_folder + "/ex0" + (str)(i))
	os.mkdir(main_folder + "/ex0" + (str)(i) + "/src")
	os.mkdir(main_folder + "/ex0" + (str)(i) + "/inc")