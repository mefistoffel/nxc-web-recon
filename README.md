# NetExec HTTP Title Protocol Module

A custom native protocol for **NetExec (NXC)** designed for rapid web reconnaissance. This module allows you to grab HTTP(S) `<title>` tags across large networks without the overhead of database management.

## 🚀 Features 
**Fast Scanning:** Uses low-level socket checks to verify port status before initiating HTTP requests. - **Dynamic Port Support:** Fully compatible with the --port` flags (e.g., `--port 8080`, `--port 8000`). - **Auto-HTTPS:** Automatically switches to `https://` schema for ports 443 and 8443. - **Clean Output:** Displays HTTP status codes and sanitized page titles directly in the NXC console. - **Native Integration:** Follows the NXC protocol folder structure for better compatibility.


## 🛠 Installation

### 1. Start a Listener

```bash
git clone [https://github.com/YOUR_USERNAME/nxc_http_module.git]
cd nxc_http_module
```


### 2.Copy files to the NetExec protocols directory:

You need to copy both the main script and the protocol folder to your NXC installation (usually found in your Python site-packages):

```bash
sudo cp http.py /usr/lib/python3/dist-packages/nxc/protocols/
sudo cp -r http/ /usr/lib/python3/dist-packages/nxc/protocols/
```

## 💻 Usage

Scan a network on the default HTTP port (80):

```bash
nxc http 192.168.1.0/24
```

Scan a custom port (e.g., 8080) and grab titles:

```bash
nxc http 192.168.1.0/24 --port 8080
```

Scan for SSL services on port 443:

```bash
nxc http 10.0.0.0/24 --port 443
```


### 🖥 Result Example

When you run the module against a network, the output will look like this:

```bash
nxc http 192.168.20.0/24 --port 8080
```

**Output:**

```bash
HTTP        192.168.20.10   8080   WEB-SRV-01       [+] HTTP 200 | Title: Dashboard - Grafana
HTTP        192.168.20.45   8080   DEV-NODE         [+] HTTP 403 | Title: Access Forbidden
HTTP        192.168.20.134  8080   GATEWAY          [+] HTTP 200 | Title: pfSense - Login
HTTP        192.168.20.150  8080   PRINTER-01       [+] Port 8080 is OPEN (No HTTP response)
```

## ⚖️ Legal Disclaimer

> [!WARNING] **For Educational and Ethical Use Only.**

This project and its source code are intended **strictly for educational purposes**, authorized security auditing, and penetration testing environments (such as HTB, THM, or private labs).

1. **Usage for illegal activities** is strictly prohibited and may lead to severe legal consequences.
    
2. **The author** assumes no liability and is not responsible for any misuse or damage caused by this tool.
    
3. **Always obtain explicit written consent** before testing any system or network that you do not own.
    

By using this software, you agree to take full responsibility for your actions. 🛡️
