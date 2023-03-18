import csv
import os
import subprocess
import PySimpleGUI as sg


# import re


def printRoute():
    # os.system('route print')
    # output = subprocess.check_output('route print', shell=True)
    # add new function to refine the output
    output = subprocess.check_output('route print', stderr=subprocess.STDOUT, text=True)
    # output = subprocess.run('dir',shell=True)
    text1 = output.find('Persistent Routes:')
    text2 = output.find('=', text1)
    print(output[text1 : text2])
    # print(str(output))
    # if 'Persistent Routes:' in output:
    #    print("string is present")


def createRoute(IP):
    routeCommand = 'route -p add ' + IP + '.0.0 mask 255.255.0.0 ' + IP + '.40.254'
    # os.system(routeCommand)
    # output = subprocess.check_output(routeCommand, shell=True)
    output = subprocess.check_output(routeCommand, stderr=subprocess.STDOUT, text=True)
    print(output)


def deleteRoute(IP):
    routeCommand = 'route -p delete ' + IP + '.0.0 mask 255.255.0.0 ' + IP + '.40.254'
    # os.system(routeCommand)
    # output = subprocess.check_output(routeCommand, shell=True)
    output = subprocess.check_output(routeCommand, stderr=subprocess.STDOUT, text=True)
    print(output)


# IPscheme = [['ZAK','76.80'],['UAD','75.16']]
file_dir = os.path.dirname(os.path.realpath('__file__'))
# file_name = file_dir + '/routes.csv'
# print (file_name)
file = open(file_dir + '/routes.csv')
# type(file)
csvreader = csv.reader(file)
header = next(csvreader)
IPscheme = []
for row in csvreader:
    IPscheme.append(row)
# print(IPscheme)
sg.theme('Default1')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Select Site Name'), sg.DropDown([l[0] for l in IPscheme], key='-SITE-')],
          [sg.Button('Create Route'), sg.Button('Delete Route'), sg.Button('Print Route'), sg.Button('Cancel')],
          [sg.Multiline("", size=(80, 20), autoscroll=True, reroute_stdout=True, reroute_stderr=True, key='-OUTPUT-')]
          ]

# Create the Window
window = sg.Window('Static Route', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    # print(event, values[0], values[1], values[2], values[3])
    print(values["-SITE-"])
    for i in IPscheme:
        if i[0] == values["-SITE-"]:
            prefix = i[2]
    if event == 'Create Route':
        createRoute(prefix)
    elif event == 'Delete Route':
        deleteRoute(prefix)
    elif event == 'Print Route':
        printRoute()
window.close()
