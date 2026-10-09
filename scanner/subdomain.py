import argparse
import socket
import sys

def main():
    parser = argparse.ArgumentParser(description="Simple Subdomain Enumerator")
    parser.add_argument("-d", "--domain", required=True, help="Target domain (e.g., example.com)")
    parser.add_argument("-w", "--wordlist", default="common_subs.txt", help="Wordlist filename")
    args = parser.parse_args()

    print("-" * 50)
    print(f"[*] Target Domain : {args.domain}")
    print(f"[*] Wordlist File : {args.wordlist}")
    print("-" * 50)

    try:
        file = open(args.wordlist, "r")
        subdomains = file.readlines()
        file.close()
    except IOError:
        print(f"[!] Error: Wordlist file '{args.wordlist}' not found.")
        sys.exit(1)

    found_count = 0
    for sub in subdomains:
        sub_name = sub.strip()
        if sub_name:
            target = f"{sub_name}.{args.domain}"
            try:
                ip = socket.gethostbyname(target)
                print(f"[+] Found: {target:<30} | IP: {ip}")
                found_count += 1
            except socket.gaierror:
                pass

    print("-" * 50)
    print(f"[*] Scan complete. Total subdomains found: {found_count}")

if __name__ == "__main__":
    main()
