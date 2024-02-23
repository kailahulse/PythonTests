import subprocess
import time
# This file was a script used to open one server terminal and 5 client terminals to stress test students code
# This can be useful whenever you may need to open multiple terminals at once 
# you can change the functionality by changing client_command and server_command to whichever files you want to open
def open_terminal(command):
    subprocess.Popen(["cmd.exe", "/c", "start", "cmd.exe", "/k", command])

def main():
    # Command to start the server
    server_command = "python server.py"
    # Command to start the client
    client_command = "python client.py"

    # Open server terminal
    open_terminal(server_command)

    # Open five client terminals
    for i in range(5):
        open_terminal(client_command)

    # Sleep to give some time for the terminals to open
    time.sleep(5)

if __name__ == "__main__":
    main()
