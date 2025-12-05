import socket
from datetime import datetime


def scan_port(host: str, port: int) -> bool:
   
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)  
    try:
        result = s.connect_ex((host, port))  
        return result == 0
    except Exception:
        
        return False
    finally:
        s.close()


def main():
    print("[SCANNER] Simple TCP Port Scanner")
    print("[SCANNER] You are allowed to scan:")
    print("          - localhost (127.0.0.1)")
    print("          - scanme.nmap.org\n")

   
    target_host = input("Enter target host (e.g., 127.0.0.1 or scanme.nmap.org): ").strip()

    try:
        resolved_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print(f"[ERROR] Could not resolve host: {target_host}")
        return

    print(f"[SCANNER] Target: {target_host} ({resolved_ip})")

    try:
        start_port = int(input("Enter START port (1-65535): ").strip())
        end_port = int(input("Enter END port   (1-65535): ").strip())
    except ValueError:
        print("[ERROR] Ports must be integers.")
        return

    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("[ERROR] Invalid port range. Use values between 1 and 65535, and START <= END.")
        return

    print(f"\n[SCANNER] Port range: {start_port}-{end_port}")
    print(f"[SCANNER] Scan started at: {datetime.now()}\n")

    for port in range(start_port, end_port + 1):
        is_open = scan_port(resolved_ip, port)
        status = "OPEN" if is_open else "closed"
        print(f"[SCANNER] Port {port:>5}: {status}")

    print(f"\n[SCANNER] Scan finished at: {datetime.now()}")


if __name__ == "__main__":
    main()