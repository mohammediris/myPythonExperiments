import sys

def ip_addr_valid(iplist):
    os.chdir(r"D:\MyPyCodes\myPythonExperiments\udemy_app1") 
    for ip in iplist:
        ip = ip.rstrip("\n")
        octet_list = ip.split('.')

        if (
            (len(octet_list) == 4) and 
            (1 <= int(octet_list[0]) <= 223) and 
            (1 <= int(octet_list[1]) <= 254) and 
            (1 <= int(octet_list[2]) <= 254) and 
            (1 <= int(octet_list[3]) <= 254) and
            (int(octet_list[0]) != 127) and 
            (int(octet_list[0]) != 169 or int(octet_list[1]) != 254)  
            ):
            continue

        else:
            print(f"{ip} is INVALID")
            sys.exit()

#ip_addr_valid(['169.54.1.10\n','169.254.2.2\n','169.254.0.1'])
