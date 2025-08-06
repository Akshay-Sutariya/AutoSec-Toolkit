# 🔒 Port Scanner with Logging & Auto-Blocking

A Python-based network port scanner designed for **real-time detection** and **automated response**. This tool scans IP addresses or subnets for open ports, logs the results, and **automatically blocks risky ports** via UFW (Uncomplicated Firewall) to minimize attack surfaces.

## 🚀 Features

- 🔍 **Port Scanning**: TCP/UDP scan using  Python socket.
- 🧾 **Real-Time Logging**: Scan results saved with timestamps in a structured log file.
- 🛡️ **Auto-Blocking**: Instantly blocks IPs that have high-risk ports open.
- 🔧 **Customizable Rules**: Configure which ports to consider risky, block duration, and more.
- 🧠 **Modular Design**: Easily integrate into larger security monitoring or automation suites.


## ⚙️ How It Works

1. **Scan Target**  
   Define target IP(s) or subnets in the config file or via CLI input.

2. **Logging**  
   Results are logged with:
   - IP address
   - Open ports
   - Timestamp

3. **Threat Detection**  
   If risky ports (e.g., 21, 23, 445) are found:
   - The source IP is added to a blocklist.
   - UFW rule is added to deny incoming traffic.


## 🛠️ Installation

```bash
git clone https://github.com/Akshay-Sutariya/port-scanner.git
cd port-scanner
```

Make sure `ufw` is enabled and configured on your system.

## 📄 Usage

```bash
python scanner.py 
```


## 🔐 Requirements

- Python 3.8+
- `nmap` (if using external scan mode)
- `ufw` (Linux firewall)
- Internet (for optional email alerts)

## ⚠️ Disclaimer

This tool is intended for **educational and authorized use only**. Do not scan or block IP addresses without permission.

## 📢 Contributing

Pull requests and ideas are welcome!  
If you encounter any issues or have improvement suggestions, feel free to open an issue.
