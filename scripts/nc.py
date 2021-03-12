import socket
import threading
import argparse
import subprocess
import sys


# define global vars

listen = False
command = False
upload = False
execute = ""
target = ""
upload_dest = ""
port = 0


def get_argument():

    # creates parser object
    parser = argparse.ArgumentParser(description="Miuaaus in the wire....")

    parser.add_argument("-p", "--port", dest="port", help="port to bind")
    parser.add_argument("-t", "--target", dest="target", help="target machine")
    parser.add_argument("-c", "--command", dest="command", help='command to lunch')
    parser.add_argument("-u", "--upload", dest="upload_dest", help="upload destination")
    parser.add_argument("-")

    arguments = parser.parse_args()
    if not arguments.port:
        parser.error("Introduce target's Port")

    if not arguments.target:
        parser.error("Introduce gateway's IP")


        # TODO finish parse options
        # ADD command , upload

    return arguments


def main():
    global listen
    global port
    global upload
    global command
    global upload_dest
    global target


    try:
        args = get_argument()

    except argparse.ArgumentError:
        (print("use -h for help"))

    if args.port is not None:
        print('port OK')
    if args.target is not None:
        print('Target is ok')


main()






