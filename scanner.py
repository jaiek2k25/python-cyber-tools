import socket
import argparse


def scan_port(target, port, timeout=0.5):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        result = sock.connect_ex((target, port))

        if result == 0:
            return True

    except socket.error:
        pass

    finally:
        sock.close()

    return False


def main():
    parser = argparse.ArgumentParser(
        description="Simple TCP port scanner for authorized targets"
    )

    parser.add_argument(
        "target",
        help="IP address or hostname to scan"
    )

    parser.add_argument(
        "-p",
        "--ports",
        default="1-1024",
        help="Port range, for example 1-1000"
    )

    args = parser.parse_args()

    try:
        start, end = map(int, args.ports.split("-"))
    except ValueError:
        print("Invalid port range. Use format: 1-1024")
        return

    if not (1 <= start <= end <= 65535):
        print("Ports must be between 1 and 65535.")
        return

    try:
        target_ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        print("Could not resolve target.")
        return

    print(f"\nTarget : {args.target}")
    print(f"IP     : {target_ip}")
    print(f"Ports  : {start}-{end}")
    print("-" * 40)

    open_ports = []

    for port in range(start, end + 1):
        if scan_port(target_ip, port):
            print(f"[+] Port {port} is OPEN")
            open_ports.append(port)

    print("-" * 40)
    print(f"Scan complete. Open ports: {len(open_ports)}")


if __name__ == "__main__":
    main()
