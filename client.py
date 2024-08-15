import socket
def client_program():
    host = '192.168.53.11'  # IP address of the controller
    port = 5000  # Port to connect to
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    message = "Hello from the instance!"
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    print("Received from server:", data)
    client_socket.close()
if __name__ == '__main__':
    client_program()
