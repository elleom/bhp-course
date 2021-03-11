import socket
import threading
import argparse
import subprocess
import sys


# define global vars

listen = False
command = False
upload = False;
execute = "";
target = ""
upload_dest = ""
port = 0


def get_argument():

    # creates parser object
    parser = argparse.ArgumentParser(description="Miuaaus in the wire....")

    parser.add_argument("-p", "--port", dest="port", help="port to bind")
    parser.add_argument("-t", "--target", dest="target", help="target machine")

    arguments = parser.parse_args()
    if not arguments.port:
        parser.error("Introduce target's Port")
        sys.exit()
    elif not arguments.target:
        parser.error("Introduce gateway's IP")
        sys.exit()

        # TODO finish parse options
        # ADD command , upload

    return arguments

    return arguments


def main():
    global listen
    global port
    global upload
    global command
    global upload_dest
    global target

    args = get_argument()

main()






