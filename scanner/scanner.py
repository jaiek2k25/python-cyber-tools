import argparse
import socket
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
Cmnports = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
    443: "HTTPS", 445: "SMB", 3306: "MySQL", 8080: "HTTP-Proxy"
}
def grabban(sock):
    try:
        sock.settimeout(1.5)
        sock.sendall(b"HEAD / HTTP/1.1\r\nHost: localhost\r\n\r\n")
        banner = sock.recv(1024).decode(errors="ignore").strip()
        return banner.splitlines()[0] if banner else "No banner returned"
    except Exception:
        return "No banner returned"
def scan_port(target_ip, port, timeout=1.0):
    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result=sock.connect_ex((target_ip, port))
        if result==0:
            service=Cmnports.get(port, "Unknown")
            banner=grabban(sock)
            sock.close()
            return {"port": port, "state": "OPEN", "service": service, "banner": banner}
        sock.close()
        return None
    except Exception:
        return None 
def parse_ports(port_str):
    """Parses port string using basic CBSE-style loops and lists."""
    ports=[]
    parts=port_str.split(',')
    for item in parts:
        if '-' in item:
            bounds=item.split('-')
            start=int(bounds[0])
            end=int(bounds[1])
            for p in range(start, end + 1):
                if p not in ports:
                    ports.append(p)
        else:
            p=int(item)
            if p not in ports:
                ports.append(p)      
    return ports
def main():
    parser=argparse.ArgumentParser(description="Simple Multithreaded Port Scanner")
    parser.add_argument("-t", "--target",required=True,help="Target IP or Domain")
    parser.add_argument("-p", "--ports",default="1-1024",help="Port range (e.g., 1-1024)")
    parser.add_argument("-w", "--workers",type=int,default=50,help="Number of threads")
    parser.add_argument("-o", "--output",help="Output text file")
    args=parser.parse_args()
    try:
        target_ip=socket.gethostbyname(args.target)
    except socket.gaierror:
        print("[!] Error: Could not resolve target hostname.")
        sys.exit(1)
    port_list=parse_ports(args.ports)
    start_time=datetime.now()
    print("-"*50)
    print("Target IP   :",target_ip)
    print("Total Ports :", len(port_list))
    print("Max Threads :", args.workers)
    print("-" * 50)
    open_ports=[]
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures={executor.submit(scan_port, target_ip, p): p for p in port_list}
        for future in as_completed(futures):
            res = future.result()
            if res is not None:
                open_ports.append(res)
                print(f"[+] Port {res['port']} | OPEN | Service: {res['service']} | Banner: {res['banner']}")
    print("-" * 50)
    print("Scan finished. Total open ports found:", len(open_ports)
    if args.output and len(open_ports) > 0:
        file = open(args.output, "w")
        file.write("Scan Report for: " + args.target + "\n")
        file.write("Target IP: " + target_ip + "\n\n")
        for item in open_ports:
            line = f"Port {item['port']}: {item['service']} | {item['banner']}\n"
            file.write(line)
        file.close()
        print("[+] Results successfully saved to", args.output)
if __name__ == "__main__":
    main()
