import socket

def connect_to_server(host='127.0.0.1', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"connected to server at {host}:{port}")

    data = client_socket.recv(1024).decode('utf-8')
    print(f"received message: {data}")

    client_socket.close()

if __name__ == "__main__":
    connect_to_server()
