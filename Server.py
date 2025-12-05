import socket

HOST = "127.0.0.1" 
PORT = 5000     

def start_server():
 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"[SERVER] Listening on {HOST}:{PORT}")

        print("[SERVER] Waiting for a client to connect...")
        conn, addr = server_socket.accept()
        print(f"[SERVER] Connection accepted from {addr}")

        data = conn.recv(1024)
        if data:
            decoded = data.decode("utf-8")
            print(f"[SERVER] Received from client: {decoded}")

            response = "Message received loud and clear!"
            conn.sendall(response.encode("utf-8"))
            print("[SERVER] Response sent to client.")

        print("[SERVER] Closing client connection.")
        conn.close()


    except Exception as e:
        print(f"[SERVER] Error: {e}")

    finally:
        print("[SERVER] Shutting down server.")
        server_socket.close()

if __name__ == "__main__":
    start_server()
