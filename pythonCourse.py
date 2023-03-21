# import subprocess
#
# # # User input
# # # user = input("Please enter the string you want to be printed out: ")
# #
# # # Saving the input to a variable
# # # user_says = input("Please enter the string you want to be printed out: ")
# # # print(user_says)
# #
# # # variable assignment. multiple variables can be assigned in single line
# # a, b, c = 1, 2, 3
# # print(a,b,c)
# # print(id(a)) # id function will show the location of the assigned value
# #
# # # reversing a string
# # string = "my name is iris"
# # print(string[::-1]) # print each character starting from last char to first char with step size -1
# # # string syntax is string [start :stop :step]
# # # formatting string using fstring
# # model = '2600XM'
# # slots = 8
# # ios = 12.3
# # print(f"Cisco model: {model}, {slots} WAN Slots, IOS {ios}")
# #
# # print(dir(subprocess))
# #
# #
# # for i in range(10):
# #     print("hello")
#
# # while True:
# #     x = input("enter the number: ")
# #     for i in range(3):
# #         if int(x) == 5:
# #             print('a')
# #
# #         elif int(x) == 6:
# #             print('b')
# #
# #         else:
# #             print('number not 5 or 6')
# #             break
# # Python program to illustrate
# # # enumerate function in loops
# # l1 = ["eat", "sleep", "repeat"]
# #
# # # printing the tuples in object directly
# # for ele in enumerate(l1):
# # 	print (ele)
# #
# # # changing index and printing separately
# # for count, ele in enumerate(l1, 50):
# # 	print (count, ele)
# #
# # # getting desired output from tuple
# # for count, ele in enumerate(l1):
# # # 	print(count,ele)
# # # 	#print(ele)
# #
# # vendors = ["Cisco", "HP", "Nortel", "Avaya", "Juniper"]
# #
# # for element in vendors:  # interating over a sequence and executing the code indented under the "for" clause for each element in the sequence
# #     print(element)
# # # else:  # the indented code below "else" will be executed when "for" has finished looping over the entire list
# # print("The end of the list has been reached")
#
# def my_first_function(*args):
#     for arguments in args:
#         if arguments%2==0:
#             print("a")
#             break
#         else:
#             print(arguments**2)
#
#
# list = list(range(10))
# print(list)
# for i in list:
#     my_first_function(i,i+1,i+2)

# f = open(r"C:\Users\Mohammed Iris\PycharmProjects\myPythonExperiments\routes.csv","r")
# # r is mentioned before quotes to
# # consider the path as literal string instead of unicode characters like \n \U\T
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readlines())

# newfile = open(r"C:\Users\Mohammed Iris\PycharmProjects\myPythonExperiments\sample.txt","a")
# newfile.write("hi there how are you?, I am good \n ")
# newfile.close()
# newfile = open(r"C:\Users\Mohammed Iris\PycharmProjects\myPythonExperiments\sample.txt","r")
# print(newfile.readlines())
# with open(r"C:\Users\Mohammed Iris\PycharmProjects\myPythonExperiments\sample.txt","a+") as readFile:
#
#     print(readFile.read())
#     readFile.write("this is my second line \n ")
#     readFile.seek(0)
#     print(str(readFile.read()))
#
# import re
#
# str = "aa  cc"
# try:
#     result = re.search(r"b{1,3}",str)
#     print(result.group())
# except AttributeError:
#     print("no match found")


a= lambda x:[x for x in range(10)]+x

print(a([2,3,4]))