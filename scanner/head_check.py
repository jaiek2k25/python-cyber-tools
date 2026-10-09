import argparse
import urllib.request
import urllib.error
import sys

SEC_HEADERS = {
    "Strict-Transport-Security": "Enforces secure HTTPS connections (HSTS)",
    "Content-Security-Policy": "Prevents Cross-Site Scripting (CSP)",
    "X-Frame-Options": "Prevents Clickjacking attacks",
    "X-Content-Type-Options": "Prevents MIME-type sniffing",
    "X-XSS-Protection": "Legacy browser XSS filter"
}

def check_headers(url):
    try:
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url
        req = urllib.request.Request(url, headers={'User-Agent': 'CyberSecurityStudent/1.0'})
        response = urllib.request.urlopen(req, timeout=5)
        return url, dict(response.headers), None
    except urllib.error.HTTPError as e:
        return url, dict(e.headers), None
    except Exception as err:
        return url, None, str(err)

def main():
    parser = argparse.ArgumentParser(description="Web Header Security Inspector")
    parser.add_argument("-u", "--url", required=True, help="Target URL or Domain")
    parser.add_argument("-o", "--output", help="Save security audit report to a text file")
    args = parser.parse_args()

    print("-" * 65)
    print(f"[*] Auditing Target URL: {args.url}")
    print("-" * 65)

    target_url, headers, error = check_headers(args.url)

    if error:
        print(f"[!] Connection Error: {error}")
        sys.exit(1)

    found_headers = []
    missing_headers = []

    for header, description in SEC_HEADERS.items():
        matched_key = None
        for h in headers:
            if h.lower() == header.lower():
                matched_key = h
                break
        
        if matched_key:
            found_headers.append((header, headers[matched_key]))
            print(f"[+] [PRESENT] {header}")
        else:
            missing_headers.append((header, description))
            print(f"[-] [MISSING] {header} — ({description})")

    print("-" * 65)
    score = len(found_headers)
    total = len(SEC_HEADERS)
    print(f"[*] Security Header Score: {score} / {total} implemented")

    if args.output:
        file = open(args.output, "w")
        file.write("Web Header Security Audit Report\n")
        file.write("Target: " + target_url + "\n")
        file.write(f"Score: {score}/{total} Headers Implemented\n\n")
        
        file.write("--- PRESENT HEADERS ---\n")
        for h, val in found_headers:
            file.write(f"{h}: {val}\n")
            
        file.write("\n--- MISSING HEADERS ---\n")
        for h, desc in missing_headers:
            file.write(f"{h} (Missing) | Purpose: {desc}\n")
            
        file.close()
        print(f"[+] Report saved successfully to '{args.output}'")

if __name__ == "__main__":
    main()
