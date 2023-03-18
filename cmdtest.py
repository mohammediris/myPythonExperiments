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
ch = ['add','delete']
IPscheme = [['ZAK','76.80'],['UAD','75.16']]
print('enter site prefix in CAPS')
siteName = input()
print('press 1 to create route\npress 2 to delete route')
choice = input()

for i in IPscheme:
    if (i[0] == siteName):
        prefix = (i[1])
        if int(choice) == 1:
            createRoute(prefix)
        else:
            deleteRoute(prefix)








