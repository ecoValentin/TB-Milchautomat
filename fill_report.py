import os, sys
import glob
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json as json_lib

def send_email(subject, body, to_email):
    """Send an email with the specified subject and body to the given recipient."""
    from_email = "" # Enter Email Address
    password = ""   #Enter Password
    server = smtplib.SMTP('mail.your-server.de', 587)  # Replace with your SMTP server and port

    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # Start the SMTP server
    server.starttls()
    server.login(from_email, password)

    # Send the email
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

if __name__ == "__main__":
    directory = "/home/pi/Automat/DEBUG/Logging/Tank/"  # Replace with the actual directory path
    target_day = "2025-03-18" 
    if len(sys.argv) > 1:
        target_day = sys.argv[1]
    
    # Construct the file path for the target day's log file
    log_file_path = os.path.join(directory, f"{target_day}.log")

    # Check if the file exists
    if not os.path.exists(log_file_path):
        print(f"Log file for {target_day} not found at {log_file_path}.")
        sys.exit(1)

    # Read the content of the log file
    with open(log_file_path, 'r') as log_file:
        lines = log_file.readlines()
        json = lines[-1].strip()  # Get the last line

    # Parse the JSON string
    data = json_lib.loads(json)

    # Extract the filling levels from the JSON payload
    filling_level_tank1 = data["LogMsg"]["payload"]["fillingLevelTank1"]
    filling_level_tank2 = data["LogMsg"]["payload"]["fillingLevelTank2"]

    # Assign the extracted values to variables
    total_milk_sold = filling_level_tank1
    total_euro_received = filling_level_tank2

    subject = f"Milchautomat Tankstand {target_day}"
    body = f"Der Tankstand am {target_day} ist: \r\n\r\nTank 1: {total_milk_sold:.2f}L\r\nTank 2: {total_euro_received:.2f}L"
    to_email = "v@gritsch.me"  # Replace with the recipient's email
    
    send_email(subject, body, to_email)
    print(f"On {target_day} Tank 1 is at: {total_milk_sold:.2f}L, Tank 2 bei {total_euro_received:.2f}L.")


