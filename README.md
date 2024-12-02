# Automated Backup Script

## Overview

This Python script automates the backup of important files by creating a compressed archive, managing backup retention, and sending email notifications about the backup status. It ensures data safety with automated processes for backup creation and cleanup.

---

## Features

- **Automated Backup Creation:** Compresses files from a specified source directory into a timestamped ZIP archive.
- **Retention Management:** Deletes old backups beyond a configurable retention period.
- **Email Notifications:** Sends an email notification upon successful or failed backup attempts.

---

## Requirements

- Python 3.x
- Required modules:
  - `os`
  - `datetime`
  - `zipfile`
  - `smtplib`
  - `email.mime.text`

---

## Configuration

Customize the following variables in the script according to your needs:

### Directories:
- `source_dir`: Path to the directory containing files to be backed up.
- `backup_dir`: Path to store the backup archives.

### Backup Retention:
- `retention_days`: Number of days to keep old backups.

### Email Settings:
- `email_notifications`: Set to `True` to enable email notifications.
- `email_recipient`: Email address to receive notifications.
- `email_sender`: Sender's email address.
- `smtp_server`: SMTP server address (default: `smtp.gmail.com`).
- `smtp_port`: Port for the SMTP server (default: `587`).
- `smtp_user`: SMTP user email.
- `smtp_pass`: SMTP user password (ensure this is secure).

---

## Usage

1. Clone or download this repository.
2. Update the configuration section with your specific directories and email settings.
3. Run the script using:

   ```bash
   python backup_script.py
   ```

---

## Example Configuration

```python
source_dir = "/home/kali/Desktop/important_files"
backup_dir = "/home/kali/Desktop/backups"
retention_days = 7
email_notifications = True

email_recipient = "example_recipient@gmail.com"
email_sender = "example_sender@gmail.com"
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_user = "your_email@gmail.com"
smtp_pass = "your_email_password"
```

---

## License

This project is licensed under the MIT License.

---

### Author

Developed by Mohamed Ahsan Wakir & Abdullah Maqbool.
