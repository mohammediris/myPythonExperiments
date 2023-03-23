import os.path
import sys

def ip_file_valid():
    # this code is to verify if the specified file is existing or not
    # following code will change the working directory to the path specified
    # so that the files can be called without writing the whole path
    os.chdir(r"D:\MyPyCodes\myPythonExperiments\udemy_app1") 
    ip_file = input("Enter the file name: ")

    if os.path.isfile(ip_file) == True:
        print("\n IP File is valid \n")
    else:
        print(f"File {ip_file} does not exist")
        sys.exit()

    selected_ip_file = open(ip_file, 'r')

    selected_ip_file.seek(0)

    ip_list = selected_ip_file.readlines()

    selected_ip_file.close()    

    return ip_list

