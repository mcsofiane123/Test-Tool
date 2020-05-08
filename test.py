import socket
import sys

print("Enter Your Web target: ")
hostname=input()
ip=socket.gethostbyname(hostname)
print("Host Name is: ",hostname)
print("IP Web Target is: ",ip)
