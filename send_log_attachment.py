import os
import datetime
import yagmail

=== CONFIGURATION ===
LOG_DIR = os.environ.get("LOG_DIR", "/")
EMAIL_USER = os.environ.get("SENDER_USERNAME")  
EMAIL_PASSWORD = os.environ.get("SENDER_PASSWORD") 
RECIPIENT = os.environ["MAIL_RECIPIENTS"]  
# 


def get_yesterdays_log_file():
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    log_filename = f"logfile_45-debris-crane.log.{yesterday.strftime('%Y-%m-%d')}"
    full_path = os.path.join(LOG_DIR, log_filename)

    if os.path.isfile(full_path):
        return full_path
    return None

def send_email_with_attachment(file_path):
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    date_str = yesterday.strftime("%Y-%m-%d")
    # Dynamic subject with date
    subject = f"Everyday Scheduled Logs from Shark System - {date_str}"
    body = """
        Hi Shark Support Team,

        I hope you're doing well.

        Please find attached the log file for your review. Kindly check it and let us know if you identify any inconsistencies or issues that require attention.

        Thank you for your continued support. 
        """
    try:
        yag = yagmail.SMTP(EMAIL_USER, EMAIL_PASSWORD)
        yag.send(to=RECIPIENT, subject=subject, contents=body, attachments=[file_path])
        print(f" Email sent with attachment: {file_path}")
    except Exception as e:
        print(f" Failed to send email: {e}")

if __name__ == "__main__":
    log_file = get_yesterdays_log_file()
    if log_file:
        send_email_with_attachment(log_file)
    else:
        print("No log file found for yesterday.")
