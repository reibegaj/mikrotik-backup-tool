from librouteros import connect
from getpass import getpass
import simplejson as json

ip_address = input ("Input router's IP Address:") 

#ip_address = ["192.168.77.1"]

user= input ("Input username: ")
passw = getpass()

for ip in ip_address:
    api = connect(username=user, password=passw, host=ip_address)
    ip_info = api(cmd="/export =file=backuppython")
    print (json.dumps(ip_info, indent=3, iterable_as_array=True))
