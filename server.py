import socket

def start_server(host='0.0.0.0', port=12345):
    # creating the socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}...")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")
        
        # a message to the client
        message = "Hello from the server!"
        client_socket.send(message.encode('utf-8'))
        
        # Close the connection
        client_socket.close()
        print(f"Connection with {client_address} closed.")

if __name__ == "__main__":
    start_server()


