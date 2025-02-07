import os
import time
import requests
import html
import string  # Added import for string module
from pystyle import Write, Colors
from colorama import Fore, init
import random

init(autoreset=True)

Write.Print(r"""
█████ █   █ ████ █   █  █    ███   ██  █████  ███  █    ████
█    █ █  █ █    █   █  █    █  ███ █  █   █   █   █    ██
█████   █   ██   █   █  █    █      █  █████   █   █      ██
█      █    ███   ███   ████ █      █  █   █  ███  ███  ████
            Made by the husband of Pyeul lihm
[1] Generate Mail
[2] Exit
""", Colors.blue_to_white, interval=0.0001)

# Your Mailgun API Credentials
DOMAIN = "pyeulmails.reyzhaven.com"  # Replace with your actual domain
API_KEY = "ed581be8c68c544673766386dc4c618d-667818f5-ec613600"  # Replace with your actual Mailgun API key
MAILGUN_INBOX_API = f"https://api.mailgun.net/v3/{DOMAIN}/events"
MAILGUN_API_URL = f"https://api.mailgun.net/v3/{DOMAIN}/messages"

def generate_random_email():
    """Generate a random temporary email."""
    random_string = "".join(random.choices(string.ascii_lowercase + string.digits, k=12))
    return f"{random_string}@{DOMAIN}"

def send_email_to_generated_address(email):
    """Send a test email to the generated email address using Mailgun."""
    data = {
        "from": f"Temp Mail Service <no-reply@{DOMAIN}>",
        "to": email,
        "subject": "Facebook OTP - Your Code",
        "text": f"Hello! This is a test email sent to your temporary address: {email}. Your OTP is 123456.",
    }

    response = requests.post(
        MAILGUN_API_URL,
        auth=("api", API_KEY),
        data=data
    )

    if response.status_code == 200:
        print(Fore.GREEN + f"[+] Test email sent to {email}")
    else:
        print(Fore.RED + "[!] Error sending test email.")

def fetch_inbox_emails():
    """Fetch incoming emails from Mailgun's inbox."""
    response = requests.get(
        MAILGUN_INBOX_API,
        auth=("api", API_KEY),
        params={"event": "delivered", "limit": 5}  # Limit to 5 emails for testing
    )

    if response.status_code == 200:
        emails = response.json().get('items', [])
        return emails
    else:
        print(Fore.RED + f"[!] Error fetching emails: {response.json()}")
        return []

def check_for_otp(emails):
    """Check if any email contains an OTP."""
    print(Fore.YELLOW + "[!] Checking for OTP emails...")

    if emails:
        for email in emails:
            subject = email['message']['headers']['subject']
            body_text = email['message']['body']['text']

            if "Facebook OTP" in subject:  # Filter based on subject
                print(Fore.CYAN + f"\n[+] New message with OTP:")
                print(Fore.WHITE + f"Subject: {subject}")
                print(Fore.WHITE + f"Body: {body_text}\n")
            else:
                print(Fore.YELLOW + f"[!] Non-OTP Email: {subject}")
    else:
        print(Fore.YELLOW + "[!] No new emails found.")

def generate_mail():
    print(Fore.YELLOW + "[!] Generating email, please wait...")
    time.sleep(1.5)

    # Generate a random email address
    temp_email = generate_random_email()
    print(Fore.GREEN + f"[+] Generated temporary email: {temp_email}")

    # Send test email to the generated address
    send_email_to_generated_address(temp_email)

    print(Fore.YELLOW + "[!] Waiting for messages... (This may take a few minutes)")
    start_time = time.time()

    while True:
        # Fetch inbox emails
        emails = fetch_inbox_emails()
        check_for_otp(emails)

        # Check if 50 seconds have passed and show the exit prompt
        elapsed_time = time.time() - start_time
        if elapsed_time >= 50:
            if exit_prompt():
                break
            else:
                start_time = time.time()  # Reset the timer after prompt

        time.sleep(15)  # Recheck every 15 seconds

def exit_prompt():
    opc = Write.Input('\nWould you like to exit? (y/n): ', Colors.blue_to_white)
    if opc.strip().lower() == 'y':
        print(Fore.GREEN + "Exiting...")
        return True
    elif opc.strip().lower() == 'n':
        print(Fore.YELLOW + "Continuing to check for messages...")
        return False
    else:
        print(Fore.RED + "Invalid input! Please type 'y' for Yes or 'n' for No.")
        return exit_prompt()

while True:
    opc = Write.Input('\nroot@mail>> ', Colors.blue_to_white)
    if opc.strip() == '1':
        generate_mail()  # Generate mail and wait for new messages
    elif opc.strip().lower() == '2' or opc.strip().lower() == 'exit':
        print(Fore.GREEN + "Exiting...")
        break
    else:
        print(Fore.RED + "Invalid option!")
