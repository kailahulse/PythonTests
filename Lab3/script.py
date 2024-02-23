import subprocess
import time

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