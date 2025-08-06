import os
import hashlib
import json
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


BASELINE_FILE = "baseline.json"
LOG_FILE = "fim_log.txt"

def get_file_hash(path):
    sha256 = hashlib.sha256()
    try:
        with open(path, 'rb') as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        return None

def scan_directory(directory):
    hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            file_hash = get_file_hash(full_path)
            if file_hash:
                hashes[full_path] = file_hash
    return hashes

def save_baseline(hashes):
    with open(BASELINE_FILE, 'w') as f:
        json.dump(hashes, f, indent=2)

def load_baseline():
    if not os.path.exists(BASELINE_FILE):
        return {}
    with open(BASELINE_FILE, 'r') as f:
        return json.load(f)

def compare_hashes(old, new):
    modified = []
    deleted = []
    added = []

    for path in old:
        if path not in new:
            deleted.append(path)
        elif old[path] != new[path]:
            modified.append(path)

    for path in new:
        if path not in old:
            added.append(path)

    return modified, deleted, added

def log_changes(modified, deleted, added):
    with open(LOG_FILE, 'a') as log:
        log.write(f"\n--- Scan at {datetime.now()} ---\n")
        for f in modified:
            log.write(f"[MODIFIED] {f}\n")
        for f in deleted:
            log.write(f"[DELETED]  {f}\n")
        for f in added:
            log.write(f"[ADDED]    {f}\n")
            
def send_email_alert(subject, message):
    sender_email = "sender@gmail.com"
    receiver_email = "receiver@gmail.com"
    password = "abcd xyze abcd xyze"  # Use app password for Gmail!

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.send_message(msg)
            print("[+] Email alert sent.")
    except Exception as e:
        print(f"[-] Failed to send email: {e}")


def main():
    target = "./test"

    print("[*] Scanning directory...")
    new_hashes = scan_directory(target)

    if not os.path.exists(BASELINE_FILE):
        print("[+] Creating baseline...")
        save_baseline(new_hashes)
        print("Baseline saved.")
    else:
        old_hashes = load_baseline()
        modified, deleted, added = compare_hashes(old_hashes, new_hashes)
        if modified or deleted or added:
        	message = "File Integrity Alert:\n\n"
        	if modified:
        		message += "Modified:\n" + "\n".join(modified) + "\n\n"
        	if deleted:
        		message += "Deleted:\n" + "\n".join(deleted) + "\n\n"
        	if added:
        		message += "Added:\n" + "\n".join(added) + "\n\n"
        send_email_alert("File Integrity Alert - Changes Detected", message)

        log_changes(modified, deleted, added)

        if modified or deleted or added:
            print("[!] Changes detected. Check fim_log.txt.")
        else:
            print("[✓] No changes detected.")

if __name__ == "__main__":
    main()
