import socket
import argparse
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init
import threading

# initialize colorama
init(autoreset=True)

lock = threading.Lock()  # for safe file writes

def scan_port(ip, port, output_file=None):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))

        if result == 0:  # only show open ports
            try:
                banner = sock.recv(1024).decode(errors="ignore").strip()
            except:
                banner = "No banner"
            line = f"{Fore.GREEN}[OPEN]{Style.RESET_ALL} {ip}:{port} | {banner}"

            print(line)
            if output_file:
                with lock:
                    with open(output_file, "a") as f:
                        f.write(line + "\n")

        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Simple Port Scanner with Banner Grabbing")
    parser.add_argument("-t", "--target", required=True, help="Target IP or domain")
    parser.add_argument("-p", "--ports", default="1-1024", help="Port range, e.g., 1-1000")
    parser.add_argument("-o", "--output", help="Save results to file")

    args = parser.parse_args()

    try:
        ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        print(f"{Fore.RED}Error: Could not resolve hostname {args.target}{Style.RESET_ALL}")
        return

    try:
        start_port, end_port = map(int, args.ports.split("-"))
        if start_port > end_port or start_port < 1 or end_port > 65535:
            raise ValueError
    except ValueError:
        print(f"{Fore.RED}Error: Invalid port range '{args.ports}'. Use format like 20-80.{Style.RESET_ALL}")
        return

    print(f"Scanning target {args.target} ({ip}) from port {start_port} to {end_port}...\n")

    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [
            executor.submit(scan_port, ip, port, args.output)
            for port in range(start_port, end_port + 1)
        ]
        for f in futures:
            f.result()  # wait for all to finish


if __name__ == "__main__":
    main()
