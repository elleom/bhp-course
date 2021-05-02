import socket

target_address_port = ("www.google.com", 80)

# create UDP sockect
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send
message = str.encode("something")

client.sendto(message, target_address_port)

# receive
data = client.recvfrom(4096)

print(data)
client.close()
