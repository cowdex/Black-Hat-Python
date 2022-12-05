#!/bin/python3

import argparse
import socket
import threading
import sys
import textwrap
import subprocess
import shlex 

#The shlex module implements a class for parsing simple shell-like syntaxes.
#subprocess process-creation inter-face

def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDERR)

    return output.decode()
#The argparse module makes it easy to write user-friendly command-line interfaces.
parser = argparse.ArgumentParser(
    description = "Dhik Networking Tool", # give more control over how textual descriptions are displayed.
    formatter_class = argparse.RawDescriptionHelpFormatter,
    epilog = textwrap.dedent('''Examples:
        netcat.py -t 192.168.1.108 -p 5555 -l -c # command shell
        netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.txt # upload to file
        netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\" # execute command
        echo 'ABC' | ./netcat.py -t 192.168.1.108 -p 135 # echo text to server port 135
        netcat.py -t 192.168.1.108 -p 5555 # connect to server
    '''))
parser.add_argument('-c', '--command', action='store_true', help='command shell')
parser.add_argument('-e', '--execute', help='execute specified command')
parser.add_argument('-l', '--listen', action='store_true', help='listen')
parser.add_argument('-p', '--port', type=int, default=5555, help='specified port')
parser.add_argument('-t', '--target', default='192.168.1.203', help='specified IP')
parser.add_argument('-u', '--upload', help='upload file')
args = parser.parse_args()
if args.listen:
    buffer = ''
else:
    buffer = sys.stdin.read()

nc = NetCat(args, buffer.encode())
nc.run()


