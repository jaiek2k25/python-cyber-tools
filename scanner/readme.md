# 🐍 Python Cyber Tools

A collection of custom security scripts and network reconnaissance tools written in Python 3 for learning **networking, web security, and cybersecurity fundamentals**.

---

## 🛠️ Tool 1: Multithreaded TCP Port Scanner (`scanner.py`)

A high-speed TCP port scanner utilizing concurrent thread pools for fast network discovery and service banner grabbing.

### 📌 Features
- Multithreaded TCP port scanning
- IP address and hostname resolution
- Custom port ranges and comma-separated lists (`1-1024`, `22,80,443`)
- Service banner grabbing on open sockets
- Adjustable thread worker count and connection timeout
- Basic error handling & CLI interface
- Optional export of scan results to a text file

### 📦 Libraries & Modules
- Python 3 standard libraries only (no external `pip` dependencies):
  - `argparse` (Command-line argument parsing)
  - `socket` (Low-level TCP/IP network socket operations)
  - `sys` (System-specific parameters and exit handling)
  - `concurrent.futures` (`ThreadPoolExecutor`, `as_completed` for parallel multithreading)
  - `datetime` (Scan duration tracking and timestamping)

---

## 🛡️ Tool 2: Web Header Security Inspector (`header_checker.py`)

An automated web response auditor that inspects target URLs for missing defensive security headers to prevent common client-side web vulnerabilities.

### 📌 Features
- Automated HTTP response header auditing
- Checks for critical security headers (HSTS, CSP, X-Frame-Options, X-Content-Type-Options, X-XSS-Protection)
- Target URL and domain processing with custom user-agent headers
- Graceful handling of HTTP error responses (e.g., 403/404)
- Command-line interface with score evaluation (`X/5` implemented)
- Optional report generation and file export

### 📦 Libraries & Modules
- Python 3 standard libraries only:
  - `argparse` (Command-line argument parsing)
  - `urllib.request` (Opening and reading URLs)
  - `urllib.error` (Handling HTTP and URL exceptions)
  - `sys` (System-level error exits)

---

## 📁 Project Structure

```text
python-cyber-tools/
├── scanner.py
├── header_checker.py
└── README.md
