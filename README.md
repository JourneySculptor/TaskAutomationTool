# task-automation-tool

This repository contains a Python script that automates file backup and sends email notifications. It is designed for regular file backups and daily email reminders to ensure data security.

## Features
- **Automated Backup**: Copies files from a source folder to a backup location.
- **Email Notifications**: Sends an email notification after each backup.
- **Scheduling**: Runs the backup and email tasks at specified times every day.

## Requirements
- Python 3.6+
- Required Libraries:
  - `schedule` (Install with `pip install schedule`)

## Usage

1. **Clone the repository**:

    ```bash
    git clone https://github.com/YourUsername/task-automation-tool.git
    ```

2. **Set up folder paths**:
   - In `task_automation_tool.py`, update `source_folder` and `backup_folder` variables with your desired source and backup paths.

3. **Configure email settings**:
   - Set up environment variables for your email configuration to ensure safety:
     - `SENDER_EMAIL`: Your email address (used as sender)
     - `RECEIVER_EMAIL`: The recipient’s email address
     - `EMAIL_PASSWORD`: Password for your email account
   - Alternatively, directly edit these variables in the script, but be cautious not to expose sensitive information.

4. **SMTP Server**:
   - Update the SMTP server setting in the script to match your email provider:
     - For Gmail, use `smtp.gmail.com` and port `465`.

5. **Run the script**:

    ```bash
    python task_automation_tool.py
    ```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
JourneySculptor
