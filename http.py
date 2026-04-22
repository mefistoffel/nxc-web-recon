import socket
import requests
import re
import urllib3
from nxc.connection import connection
from nxc.logger import NXCAdapter

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class http(connection):
    def __init__(self, args, db, host):
        self.protocol = "HTTP"
        if hasattr(args, 'port') and args.port:
            self.port = int(args.port)
        else:
            self.port = 80
        super().__init__(args, db, host)

    def proto_logger(self):
        self.logger = NXCAdapter(
            extra={
                "protocol": "HTTP",
                "host": self.host,
                "port": self.port,
                "hostname": self.hostname,
            }
        )

    def create_conn_obj(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.7)
            result = s.connect_ex((self.host, self.port))
            s.close()
            return result == 0
        except:
            return False

    def proto_flow(self):
        self.proto_logger()
        if self.create_conn_obj():
            schema = "https" if self.port in [443, 8443] else "http"
            url = f"{schema}://{self.host}:{self.port}"
            
            try:
                r = requests.get(url, verify=False, timeout=2, allow_redirects=True)
                
                title_search = re.search(r'<title>(.*?)</title>', r.text, re.I | re.S)
                
                if title_search:
                    raw_title = title_search.group(1).strip()
                    clean_title = " ".join(raw_title.split())
                    display_title = (clean_title[:55] + '...') if len(clean_title) > 55 else clean_title
                else:
                    display_title = "No Title Found"
                
                self.logger.success(f"HTTP {r.status_code} | Title: {display_title}")
                
            except Exception:
                self.logger.success(f"Port {self.port} is OPEN (No HTTP response)")
