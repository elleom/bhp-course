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


class NetCat:
    def __init__(self, args, buffer=None):  # constructor
        self.args = args
        self.buffer = buffer
        self.buffer = buffer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # tcp conn
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        def run(self):
            if self.args.listen:
                self.listen()  # calls to listen method
            else:
                self.send()  # calls to send method

        def send(self):
            self.socket.connect((self.args.target, self.args.port))  # connects to the target
            if self.buffer:  # if buffer sends it
                self.socket.send(self.buffer)

            try:  # supports CTRL+C KeyboardInterrupt -> close connection
                while True:
                    recv_len: 1
                    response = ''
                    while recv_len:
                        data = self.socket.recv(4096)
                        recv_len = len(data)
                        response += data.decode()
                        if recv_len < 4096:
                            break  # breaks loop if no data incoming
                        if response:
                            print(response)
                            buffer = input('> ')  # prompt
                            buffer += '\n'
                            self.socket.send(buffer.encode())  # sends input and continues loop
            except KeyboardInterrupt:
                print('User Terminated')
                self.socket.close()
                sys.exit()

        def listen(self):
            self.socket.bind((self.args.target, self.args.port))
            self.socket.listen(5)
            while True:
                client_socket, _ = self.socket.accept()
                client_thread = threading.Thread(
                    target=self.handle, args=(client_socket,)
                )
                client_thread.start()

        # executes the task corresponding to the command line argument it receives
        # if command then passes to the execute func and passes the output back on the socket.
        def handle(self, client_socket):
            if self.handle.execute:
                output = execute(self.args.execute)
                client_socket.send(output.encode())
            elif self.args.upload:
                file_buffer = b''
                while True:
                    data = client_socket.recv(4096)
                    if data:
                        file_buffer += data
                    else:
                        break
                with open(self.args.upload, 'wb') as f:
                    f.write(file_buffer)
                message = f'Saved File {self.args.upload}'
                client_socket.send(message.encode())

            elif self.args.command:
                cmd_buffer = b''
                while True:
                    try:
                        client_socket.send(b'BHP: #> ')
                        while '\n' not in cmd_buffer.decode():  # if no new line in buffer -> see @line 50
                            cmd_buffer += client_socket.recv(64)
                        response = execute(cmd_buffer.decode())
                        if response:
                            client_socket.send(response.encode())
                        cmd_buffer = b''
                    except Exception as e:
                        print(f'server killed {e}')  # print stacktrace
                        self.socket.close()
                        sys.exit()


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
    # "store_true". if the option is specified,
    # assign the value True to args.verbose. Not specifying it implies False.

    parser.add_argument('-e', '--execute', help='execute specified command')
    parser.add_argument('-l', '--listen', action='store_true', help='listen')
    parser.add_argument('-p', '--port', default=5555, help='specified port')
    parser.add_argument('-t', '--target', default='192.168.1.203', help='specified target')
    parser.add_argument('-u', '--upload', help='upload file')
    args = parser.parse_args()  # get arguments

    if args.listen: # if option set
        buffer = ''
    else:
        buffer = sys.stdin.read()
    nc = NetCat(args, buffer.encode())
    nc.run()









