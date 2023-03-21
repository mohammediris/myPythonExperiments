import re
import subprocess


def validate_ipadd_regex(ip_address):
    found = re.search(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", ip_address)
    if found:
        x = found.group()
        y = x.split(".")
        for ip_byte in y:
            if int(ip_byte) > 0 and int(ip_byte) < 255:
                continue
            else:
                return False
        return True
    else:
        print("NO IP ADDRESS FOUND")


output = subprocess.check_output('ipconfig -all', stderr=subprocess.STDOUT, text=True)
# print(type(output))
found = re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", output)

with open(r"C:\Users\Mohammed Iris\PycharmProjects\myPythonExperiments\ipAdd.txt","w") as newFile:
    # for f in found:
    #     if validate_ipadd_regex(f):
    #         print(f)
    ip_list = [f for f in found if validate_ipadd_regex(f)]
    newFile.writelines(ip_list)
print(ip_list)

