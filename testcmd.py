# # def decoretor(target_function):
# #     def function_wrapper():
# #         print("===========================\n\t\t\t"+target_function()+"\n===========================\n")
# #         return
# #     return function_wrapper

# # @decoretor
# # def target_function():
# #     return "cool"

# # target_function()

# # y = list(range(100))
# # my_iter = iter(y)
# # #print (y)
# # for i in range(4):
# #     print(f"\t {next(my_iter)}\t {next(my_iter)}\t {next(my_iter)}\t {next(my_iter)}\t {next(my_iter)}")
# import subprocess
# op = subprocess.check_output('route print', stderr=subprocess.STDOUT, text=True)
# text1 = op.index("Persistent Routes:")  # index() throw error if the string is not found
# text2 = op.index("=", text1)
# op_str = op[text1:text2]
# op_str_split = op_str.split()
# op_iter = iter(op_str_split)
# op_len = len(op_str_split)
# print(f"{next(op_iter)} {next(op_iter)}")
# print("==========================================================================")
# print(f"{next(op_iter)} {next(op_iter):<12}{next(op_iter):>12}\t{next(op_iter)} {next(op_iter):>9}\t{next(op_iter):^9}")
# print("--------------------------------------------------------------------------")
# for i in range((op_len-8)//4):
#     print(f"{next(op_iter):>12}\t{next(op_iter):>16}\t{next(op_iter):>16}\t{next(op_iter):^10}")

# print("==========================================================================")
# # import threading
# # import subprocess
# # import time 
# # def my_ping ():
# #     print ("hello")
# #     time.sleep(2)
# #     print("bye")

# # threads = []
# # for i in range(3):
# #     th = threading.Thread(target = my_ping)
# #     th.start()
# #     threads.append(th)
# # for th in threads:
# #     th.join()

# # import subprocess

# # subprocess.run("ping 8.8.8.8")
# # subprocess.run("ping 1.1.1.1")

import os 

print(f"\n{os.getcwd()}\n\n")