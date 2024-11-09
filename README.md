# TaskAutomationTool

This repository contains a Python script that automates file backup and sends email notifications. It is designed for regular file backups and daily email reminders to ensure data security.

## Features
- **Automated Backup**: Copies files from a source folder to a backup location.
- **Email Notifications**: Sends an email notification after each backup.
- **Scheduling**: Runs the backup and email tasks at specified times every day.

## Requirements
- Python 3.6+
- Libraries: os, shutil, schedule, smtplib, email, datetime, time

## Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/YourUsername/TaskAutomationTool.git
    ```
2. Set your folder paths in the script (`source_folder` and `backup_folder`).
3. Configure the email settings (`sender_email`, `receiver_email`, `password`).
4. Run the script:
    ```bash
    python TaskAutomationTool.py
    ```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
