import socket
import threading
import argparse
import subprocess
import sys
import shlex
import textwrap


def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    return output.decode()  # runs a command on the local sys and returns the output


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='NC Like Tool',
                                     # Help message formatter
                                     # which retains any formatting in descriptions.
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent('''Example:
                                     nc.py -t 192.168.1.108 -p 5555 -l -c # command shell
                                     nc.py -t 192.168.1.108 -p 5555 -l -u=file.txt #upload to file
                                     nc.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\" # execute command
                                     echo 'ABC' | ./nc.py -t 192.168.1.108 -p 5555 # echo text to server port 5555
                                     nc.py -t 192.168.1.108 -p 5555 # connect to server'''))
    parser.add_argument('-c', '--command', action='store_true', help='command shell')
    parser.add_argument('-e', '--execute', help='execute specified command')
    parser.add_argument('l', '--listen', action='store_true', help='listen')
    parser.add_argument('-p', '--port', default=5555, help='specified port')
    parser.add_argument('-t', '--target', default='192.168.1.203', help='specified target')
    parser.add_argument('-u', '--upload', help='upload file')









