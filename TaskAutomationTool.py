import os
import shutil
import schedule
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import time

# Set the folder paths (modify as needed)
source_folder = 'source_folder_path'  # Example: 'C:/Users/username/Documents' 
backup_folder = 'backup_folder_path'  # Example: 'C:/Users/username/Backup' 

# Function to perform backup
def backup_files():
    try:
        # Create the backup folder if it doesn't exist
        if not os.path.exists(backup_folder):
            os.makedirs(backup_folder)
        # Back up files from the folder
        for filename in os.listdir(source_folder):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(backup_folder, filename)
            shutil.copy2(source_path, destination_path)  # Copy the file 
            print(f"Backed up {filename} to {backup_folder}")
    except Exception as e:
        print(f"Error during backup: {e}")

# Function to send email
def send_email():
    sender_email = 'your_email@example.com'
    receiver_email = 'receiver_email@example.com'
    password = 'your_password'  # Password for email account 
    # Create the email content
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = 'Scheduled Backup Notification'
    body = f"The backup was completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    message.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP_SSL('smtp.example.com', 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")

# Schedule: perform backup and email notification at set times
schedule.every().day.at("10:00").do(backup_files)
schedule.every().day.at("10:05").do(send_email)

# Loop to run the schedule
while True:
    schedule.run_pending()
    time.sleep(60)
