import socket
host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)
print("Hostname: {0}, Ip address: {1}".format(host_name, ip_address))