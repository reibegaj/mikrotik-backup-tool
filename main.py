import os
import sys
import argparse
from librouteros import connect

def get_env(args_value, env_value, key):
    if args_value:
          return args_value 
    elif env_value:
        return env_value
    else:
        return sys.exit(f"Please provide {x}")

env = {
	"username": os.environ.get('USERNAME'),
	"password": os.environ.get('PASSWORD'),
	"hostname": os.environ.get('HOSTNAME'),
	"filename": os.environ.get('FILENAME')
}

parser = argparse.ArgumentParser()
parser.add_argument("-U", "--username", help = "Specifies username to authenticate to the router")
parser.add_argument("-P", "--password", help = "Specifies password to authenticate to the router")
parser.add_argument("-H", "--hostname", help = "Specifies the IP address to connect to router")
parser.add_argument("-F", "--filename", help = "Specifies the backup's filename to be saved")
args = vars(parser.parse_args())

parameter = {
	"username": 'test',
	"password": 'test1',
	"hostname": 'test2',
	"filename": 'test3'
}

for x in parameter.keys():
	value_from_args = args.get(x)
	value_from_env = env.get(x)
	parameter[x] = get_env(value_from_args, value_from_env, x)



api = connect(username = parameter.get('username'), password = parameter.get('password'), host = parameter.get('hostname'))
script = api.path('/export')
print(tuple(script('', **{"file": parameter.get('filename')})))
