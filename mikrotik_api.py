from librouteros import connect
from getpass import getpass
import simplejson as json

ip_address = ["192.168.77.1"]

user= input ("Input username: ")
passw = getpass()

for ip in ip_address:
    api = connect(username=user, password=passw, host=ip)
    ip_info = api(cmd="/ip/address/print")
    print (json.dumps(ip_info, indent=3, iterable_as_array=True))
