import socket

address = input("Web address: ")

try:
	print("IP address: {0}".format(socket.gethostbyname(address)))
except socket.error:
	print("Error")