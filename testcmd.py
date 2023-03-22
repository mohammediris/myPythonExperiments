# def decoretor(target_function):
#     def function_wrapper():
#         print("===========================\n\t\t\t"+target_function()+"\n===========================\n")
#         return
#     return function_wrapper

# @decoretor
# def target_function():
#     return "cool"

# target_function()

# y = list(range(100))
# my_iter = iter(y)
# #print (y)
# for i in range(4):
#     print(f"\t {next(my_iter)}\t {next(my_iter)}\t {next(my_iter)}\t {next(my_iter)}\t {next(my_iter)}")
import subprocess
op = subprocess.check_output('route print', stderr=subprocess.STDOUT, text=True)
text1 = op.index("Persistent Routes:")  # index() throw error if the string is not found
text2 = op.index("=", text1)
op_str = op[text1:text2]
op_str_split = op_str.split()
op_iter = iter(op_str_split)
op_len = len(op_str_split)
print(f"{next(op_iter)} {next(op_iter)}")
print("==========================================================================")
print(f"{next(op_iter)} {next(op_iter)}\t\t{next(op_iter)}\t\t{next(op_iter)} {next(op_iter)}\t\t{next(op_iter)}")
print("--------------------------------------------------------------------------")
for i in range((op_len-8)//4):
    print(f"{next(op_iter)}\t\t{next(op_iter)}\t\t{next(op_iter)}\t\t{next(op_iter)}")

print("==========================================================================")