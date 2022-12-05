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

