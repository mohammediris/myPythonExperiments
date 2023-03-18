import PySimpleGUI as sg
import os
def printRoute ():
    os.system('cmd /c "route print"')
def createRoute (IP):
    routeCommand = 'cmd /c "route -p add ' + IP + '.40.35 mask 255.255.0.0 ' + IP + '.40.254"'
    os.system(routeCommand)
    print ('new route created')
def deleteRoute (IP):
    routeCommand = 'cmd /c "route -p delete ' + IP + '.40.35 mask 255.255.0.0 ' + IP + '.40.254"'
    os.system(routeCommand)
    print ('route deleted')

IPscheme = [['ZAK','76.80'],['UAD','75.16']]
#======================================================================================#
sg.theme('Default1')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Enter Site Name'), sg.InputText()],
            [sg.Radio('Add Route', 'num', default=True),
             sg.Radio('Delete Route', 'num'),
             sg.Radio('Print Route', 'num')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Static Route', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
# print('You entered ', values[0], values[1], values[2], values[3])
    for i in IPscheme:
        if (i[0] == values[0]):
            prefix = (i[1])
    if values[1]==True:
        createRoute(prefix)
    elif values[2]==True:
        deleteRoute(prefix)
    elif values[3]==True:
        printRoute()
window.close()