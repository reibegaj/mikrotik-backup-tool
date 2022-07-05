import sys
from librouteros import connect
from getpass import getpass

n = len(sys.argv)
print ("Name of the script:", sys.argv[0])

#ip_address = input("Input router's IP Address: ") 
#user= input ("Input username: ")
#passw = getpass()
#filename = input("Input export result filename: ")

#api = connect(username=user, password=passw, host=ip_address)
#script = api.path('/export')
#print(tuple(script('', **{"file": filename})))

#file = api.path('/file')
#print(tuple(file('print', **{"name": f"{filename}.rsc"})))
