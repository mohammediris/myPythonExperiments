# import subprocess


# p1 = subprocess.run("route print",capture_output=True, shell=True, text=True)
# print(p1.stderr)
# print(p1.stdout)

# Python program to demonstrate
# sys.exit()
import sys

age = 17

# program that stops execution if the age is less than 18.
if age < 18:
	# exits the program
	sys.exit("hello these")
    
else:
	print("Age is not less than 18")
