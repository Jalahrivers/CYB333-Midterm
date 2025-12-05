import socket

HOST = "127.0.0.1"
PORT = 5000        

def start_client():
  
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((HOST, PORT))
        print(f"[CLIENT] Connected to {HOST}:{PORT}")

        message = "Dobby is a free elf!"
        client_socket.sendall(message.encode("utf-8"))
        print(f"[CLIENT] Sent to server: {message}")

        data = client_socket.recv(1024)
        if data:
            decoded = data.decode("utf-8")
            print(f"[CLIENT] Received from server: {decoded}")

        print("[CLIENT] Closing connection.")

    except ConnectionRefusedError:
        print("[CLIENT] Connection refused. Is the server running?") 
    except Exception as e:
        print(f"[CLIENT] Error: {e}")
    finally:
        client_socket.close()


if __name__ == "__main__":
    start_client()
