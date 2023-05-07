import argparse
import json 
import paramiko
from scp import SCPClient
from time import *
from datetime import datetime

def connectionbuild():
    host = '192.168.27.126'
    port = 22
    username = 'vboxuser'
    password = ''

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh_client.connect(hostname=host, port=port, username=username, password=password)
    return ssh_client

def send_config_file(filename):
    ssh_client = connectionbuild()
    
    scp = SCPClient(ssh_client.get_transport())
    local_path = "C:\\Users\\Dell\\OneDrive\\Desktop\\HPE\\config_files\\" + filename
    remote_path = '/home/vboxuser/HPE/config_files'
    scp.put(local_path, remote_path)

def json_file_loader():
    f = open("software_requirements.json")
    file = json.load(f)
    return file

def command_parser():
    parser = argparse.ArgumentParser(description="Command Line Interface/Multi-System-Installer")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-i', '--install', action='store_true', help='Install')
    group.add_argument('-u', '--update', action='store_true', help='Update')
    parser.add_argument('-f', '--filename', type=str, nargs='+', required=True, metavar=" ", help='Filename')
    parser.add_argument('-t', '--datetime', type=str, required=True, metavar=" ", help='Datetime in ISO format')
    
    args = parser.parse_args()

    return args   

def config_file(args):
    config = json_file_loader()
    config["action"] = "install" if args.install else "update"
    config["datetime"] = args.datetime
    config["filenames"] = args.filename

    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    extension = dt.replace(" ", ".").replace(":", "-")
    return config, extension
def main():
    args = command_parser()
    config, extend = config_file(args)
    filename = "config_file" + extend + ".json"
    filepath = "config_files/" + filename
    with open(filepath, "w") as outfile:
        json.dump(config, outfile)
    
    
    send_config_file(filename)
   

if __name__ == '__main__':
    main()
    