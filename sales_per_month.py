import os, sys
import glob
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def read_log_file(file_path, target_month):
    """Read the content of a log file and extract milk sales data."""
    total_milk_sold = 0.0
    total_euro_received = 0.0
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into its components
            components = line.strip().split(',')
            if len(components) < 5:
                continue  # Skip malformed lines

            # Extract the date and amount of milk sold
            date_str = components[1]
            milk_sold = float(components[-1])/1000
            euro_received = float(components[-2])
            
            # Check if the transaction date matches one of the target months
            try:
                transaction_date = datetime.fromisoformat(date_str[:-6])  # Remove timezone information
                transaction_month = transaction_date.strftime("%Y-%m")
                if transaction_month == target_month.strftime("%Y-%m"):
                    total_milk_sold += milk_sold
                    total_euro_received += euro_received
            except ValueError:
                continue  # Skip lines with invalid date format

    return [total_milk_sold,total_euro_received]

def calculate_milk_sold(directory, target_month):
    """Calculate the total amount of milk sold in the specified and previous month."""
    # Determine the target and previous month
    target_date = datetime.strptime(target_month, "%Y-%m")
    previous_month_date = (target_date - timedelta(days=1)).replace(day=1)
    
    total_milk = 0.0
    total_euro = 0.0
    # Get all log files in the directory
    log_files = glob.glob(os.path.join(directory, 'SalesLog_' + datetime.strftime(previous_month_date, "%Y-%m") +'*.log'))
    log_files += glob.glob(os.path.join(directory, 'SalesLog_' + datetime.strftime(target_date, "%Y-%m") +'*.log'))
    
    for log_file in log_files:
        # Extract the month from the filename
        milk_array = read_log_file(log_file, target_date)
        total_milk += milk_array[0]
        total_euro += milk_array[1]
    
    return [total_milk,total_euro]

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
    # Example usage
    directory = "/home/pi/Automat/DEBUG/Logging/salesLog/"  # Replace with the actual directory path
    target_month = "2024-05" 
    if len(sys.argv) > 1:
        target_month = sys.argv[1]
    
    total_milk_sold,total_euro_received = calculate_milk_sold(directory, target_month)

    subject = f"Monatsabrechnung {target_month}"
    body = f"Der eingenommene Betrag in {target_month} beträgt: {total_milk_sold:.2f} € bei {total_euro_received:.2f} L Milch"
    to_email = "v@gritsch.me"  # Replace with the recipient's email
    
    #send_email(subject, body, to_email)
    print(f"Total amount of milk sold in {target_month} is: {total_milk_sold:.2f}€ bei {total_euro_received:.2f} L Milch")
