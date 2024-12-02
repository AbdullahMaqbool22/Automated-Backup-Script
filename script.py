import os
import datetime
import zipfile
import smtplib
from email.mime.text import MIMEText

# Configuration
source_dir = "/home/kali/Desktop/important_files"
backup_dir = "/home/kali/Desktop/backups"
retention_days = 7  # Number of days to keep backups
email_notifications = True  # Set to False to disable email notifications

# Email configuration (if email_notifications is enabled)
email_recipient = "mohamed.ahsan.official@gmail.com"
email_sender = "00mohamed00ashan00@gamil.com"
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_user = "00mohamed00ahsan00@gmail.com"
smtp_pass = "rwvs gtsi cluj ttuw"

# Create a unique backup name with date and time
date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_name = f"backup_{date}.zip"
backup_path = os.path.join(backup_dir, backup_name)

# Function to zip files


def zip_directory(src_dir, zip_file):
    with zipfile.ZipFile(zip_file, 'w') as zipf:
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, src_dir))
    print(f"Backup created at {zip_file}")

# Function to send email notifications


def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email_sender
    msg['To'] = email_recipient

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_pass)
            server.sendmail(email_sender, [email_recipient], msg.as_string())
        print("Email notification sent.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to clean up old backups


def clean_old_backups():
    now = datetime.datetime.now()
    for filename in os.listdir(backup_dir):
        file_path = os.path.join(backup_dir, filename)
        if os.path.isfile(file_path):
            file_age_days = (
                now - datetime.datetime.fromtimestamp(os.path.getmtime(file_path))).days
            if file_age_days > retention_days:
                os.remove(file_path)
                print(f"Deleted old backup: {file_path}")


try:
    # Perform backup
    zip_directory(source_dir, backup_path)

    # Clean old backups
    clean_old_backups()

    # Send success email
    if email_notifications:
        send_email("Backup Successful",
                   f"The backup was created successfully at {backup_path}")

except Exception as e:
    error_message = f"Backup failed: {e}"
    print(error_message)
    if email_notifications:
        send_email("Backup Failed", error_message)
