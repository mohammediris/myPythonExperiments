import sys
import subprocess


def ip_reach(list):
    os.chdir(r"D:\MyPyCodes\myPythonExperiments\udemy_app1") 
    for ip in list:
        ip = ip.rstrip("\n")
        ping_reply = subprocess.run(f"ping {ip} -n 2",stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
        #print(ping_reply.returncode)
        #print('\n')
       #
        if ping_reply.returncode == 0:
            print(f"{ip} is reachable")
            continue
        else:
            print(f"{ip} is not reachable ")
            continue
    
            

ip_reach(['192.168.2.11','192.168.2.12'])