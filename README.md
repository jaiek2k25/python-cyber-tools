# Python Cyber Tools

**A modular, zero-dependency cybersecurity toolkit built in pure Python 3.**

Designed for network reconnaissance and basic defensive web auditing.  
No external packages — only the Python standard library.

[![Python](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Dependencies](https://img.shields.io/badge/dependencies-none-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-green.svg)]()

---

## Tools Included

### 1. Multithreaded TCP Port Scanner (`scanner/scanner.py`)

High-speed TCP port scanner with concurrent workers and banner grabbing.

**Features**
- Multithreaded scanning using `ThreadPoolExecutor`
- Custom port ranges and individual ports
- Banner grabbing on open ports
- Adjustable thread count and timeout
- Simple CLI interface

**Example**
```bash
python scanner/scanner.py -t example.com -p 1-1024 -w 50
```

### 2. Web Header Security Inspector (`scanner/head_check.py`)

Checks a target URL for missing or weak security headers.

**Headers checked**
- Strict-Transport-Security (HSTS)
- Content-Security-Policy (CSP)
- X-Frame-Options
- X-Content-Type-Options
- X-XSS-Protection

**Example**
```bash
python scanner/head_check.py https://example.com
```

### 3. Subdomain Finder (`scanner/subdomain.py`)

Basic subdomain enumeration using a wordlist.

---

## Project Structure

```text
python-cyber-tools/
├── scanner/
│   ├── scanner.py          # Multithreaded port scanner
│   ├── head_check.py       # Security header inspector
│   ├── subdomain.py        # Subdomain finder
│   ├── common_subs.txt     # Wordlist
│   └── readme.md           # Detailed tool notes
└── README.md
```

---

## Design Philosophy

- **Zero external dependencies** — only Python standard library
- Clear CLI interfaces with `argparse`
- Focus on understanding sockets and HTTP rather than using heavy frameworks
- Suitable for learning and practical experimentation

---

## Requirements

- Python 3.8+
- No `pip install` required

---

## Notes

These tools are intended for **educational and authorized testing only**.  
Do not scan or probe systems without explicit permission.

---

Built as part of my cybersecurity learning path toward IIT B.Cyber programs.