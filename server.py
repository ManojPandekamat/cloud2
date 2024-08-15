import socket

def server_program():
    host = '0.0.0.0'  # Bind to all available interfaces
    port = 5000  # Port to listen on

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Server listening on port:", port)

    conn, address = server_socket.accept()
    print("Connection from:", address)
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("Received from client:", data)
        conn.send(data.encode())  # Echo the received data back to the client

    conn.close()

if __name__ == '__main__':
    server_program()
