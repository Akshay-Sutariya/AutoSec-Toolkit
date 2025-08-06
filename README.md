# 🛡️ File Integrity Monitoring Tool (FIM) 

A lightweight Python-based File Integrity Monitoring (FIM) tool that continuously watches a specified directory for unauthorized changes, logs them, and sends email alerts to the administrator in real-time. Ideal for detecting suspicious file activities in critical directories.

---

## 🚀 Features

- ✅ Monitors file additions, deletions, and modifications
- ✅ Calculates and compares SHA256 hashes for integrity checks
- ✅ Logs timestamped activity to a secure log file
- ✅ Sends automated **email alerts** for detected changes
- ✅ Can run continuously in the background (`nohup`) or scheduled via cron
- ✅ Easily configurable for any directory

---

## 🛠️ Requirements

- Python 3.x
- Linux (tested on Kali, Ubuntu)
- Internet connection for sending emails

### Python Libraries

```bash
pip install smtplib hashlib
```

*(Note: `hashlib` and `smtplib` are part of Python’s standard library)*

---

## 📦 Usage

### 1. **Clone the Repository**

```bash
git clone https://github.com/Akshay-Sutariya/File-Integrity-Monitor.git
cd File-Integrity-Monitor
```

### 2. **Set the Directory to Monitor**

Edit the script (e.g. `fim_tool.py`) and set the path:

```python
directory_to_monitor = "/path/to/your/directory"
```

### 3. **Configure Email Settings**

Replace with your credentials and recipient email:

```python
sender_email = "you@example.com"
receiver_email = "admin@example.com"
password = "your_app_password"
smtp_server = "smtp.gmail.com"
smtp_port = 587
```

> ⚠️ Use [App Passwords](https://support.google.com/accounts/answer/185833) if using Gmail with 2FA.

---

### 4. **Run the Tool**

#### ✅ Run Manually

```bash
python3 fim_tool.py
```

#### ✅ Run in Background (Using `nohup`)

```bash
nohup python3 fim_tool.py &
```

- Output is saved to `nohup.out`
- To stop it:

```bash
ps aux | grep fim_tool.py
kill <PID>
```

#### ✅ Schedule to Run Every Minute (Using Cron)

1. Open crontab:

```bash
crontab -e
```

2. Add this line (change path accordingly):

```bash
* * * * * /usr/bin/python3 /full/path/to/fim_tool.py
```

This runs the script every 1 minute.

---

## 📂 Logs

All detected changes are logged with timestamps in:

```
fim_log.txt
```

Example:

```
[2025-08-06 12:41:05] File Modified: /etc/passwd
```

---

## 📌 Use Cases

- Monitoring `/etc`, `/home/user/scripts`, or web directories
- Alerting sysadmins of potential intrusions
- Lightweight layer of filesystem change detection

---

## 🙋‍♂️ Author

**Akshay Sutariya**  
🔗 [GitHub: Akshay-Sutariya](https://github.com/Akshay-Sutariya)  
🎓 MSc Cybersecurity Student  
📬 Connect on [LinkedIn](https://linkedin.com)

---

## 📄 License

This project is licensed under the MIT License.
