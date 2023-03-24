import paramiko
import os.path
import time
import sys
import re


os.chdir(r"D:\MyPyCodes\myPythonExperiments\udemy_app1") 
user_file = input("Enter user file name: ")

if os.path.isfile(user_file) == True:
    print("\n User File is valid \n")
else:
    print(f"File {user_file} does not exist")
    sys.exit()

cmd_file = input("Enter cmd file name: ")

if os.path.isfile(cmd_file) == True:
    print("\n Command File is valid \n")
else:
    print(f"File {cmd_file} does not exist")
    sys.exit()

def ssh_connection(ip):

    global user_file
    global cmd_file

    try:
        selected_user_file = open(user_file,'r')
        selected_user_file.seek(0)
        username = selected_user_file.readlines()[0].split(',')[0].rstrip("\n")
        selected_user_file.seek(0)
        password = selected_user_file.readlines()[0].split(',')[1].rstrip("\n")

        session = paramiko.SSHClient()

        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        session.connect(ip.rstrip("\n"),username=username,password=password)

        connection = session.invoke_shell()

        connection.send("enable\n")
        connection.send("terminal length 0\n")
        time.sleep(1)

        connection.send("\n")
        connection.send("configure terminal\n")
        time.sleep()

        selected_cmd_file = open(cmd_file,'r')

        for each_line in selected_cmd_file.readlines()
        connection.send(each_line+'\n')
        time.sleep(2)

        selected_user_file.close()
        selected_cmd_file.close()

        router_output = connection.recv(65535)

        if re.search(b"% Invalid input", router_output)
            print(f"There was at least one IOS syntax error on device {ip}")
        else:
            print(f"DONE for device {ip}")
        print(str(router_output)+'\n')


        session.close()

    except paramiko.AuthenticationException:
        print("Invalid username or password")
        print("CLosing Program Bye...")



