import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)  # params (max backlog amount)

print("[+] Listening on %s:%d" % (bind_ip, bind_port))


# client handling thread
def handle_client(client_socket):

    # print out client request
    request = client_socket.recv(1024)

    print("[*] received: %s" % request)

    # send back AKC response
    client_socket.send("ACK".encode())

    client_socket.close()


while True:

    client, addr = server.accept()
    print("[+] Accepted connection from: %s:%d" % (addr[0], addr[1]))

    # spin up client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()

