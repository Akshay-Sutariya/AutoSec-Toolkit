
import socket
import ipaddress
import subprocess
from datetime import datetime

#settings
COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 3306, 3389]
RISKY_PORTS = [23,445,3389] # Telnet, SMB, RDP
OPEN_PORT_THRESHOLD = 10
SCAN_TIMEOUT = 1


def scan_ip(ip):
	open_ports = []
	for port in COMMON_PORTS:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.settimeout(SCAN_TIMEOUT)
			result = sock.connect_ex((str(ip), port))
			if result == 0:
				open_ports.append(port)
			sock.close()
		except:
			pass
	return open_ports


def log_result(ip,ports):
	with open("scan_results.log", "a") as f:
		f.write(f"{datetime.now()} - {ip} - Open Ports: {ports} \n")
		

def block_ip(ip):
	try:
		subprocess.run(["ufw", "deny", "from", str(ip)], check=True)
		print(f"[+] Blocked suspicious IP: {ip}")
	except Exception as e:
		print(f"[!] Failed to block {ip}: {e}")
		
				
def main():
	target = input("Enter target IP or CIDR range: ").strip()
	try:
		network = ipaddress.ip_network(target, strict=False)
	except ValueError:
		print("Invalid IP/CIDR.")
		return
	
	for ip in network.hosts():
		print(f"\n[~] Scanning {ip}")
		open_ports = scan_ip(ip)
		print(f"      Open ports: {open_ports}")
		log_result(ip, open_ports)
		
		if len(open_ports) > OPEN_PORT_THRESHOLD or any(p in RISKY_PORTS for p in open_ports):
			block_ip(ip)
			

if __name__ == "__main__":
	main()
	
