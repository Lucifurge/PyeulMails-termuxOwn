PyeulMails-termuxOwn ✨
Welcome to the PyeulMails-termuxOwn repository! 🎉 This is a Termux-based tool designed to generate temporary emails and interact with Mailgun's API. Whether you need a disposable email for testing or quick sign-ups, this tool has you covered. It also checks incoming emails for OTPs (One-Time Passwords) seamlessly!

🚀 Features
🎯 Random Temporary Email Generation: Instantly create disposable email addresses with a click.
📧 Mailgun Integration: Send and receive emails using the Mailgun API.
✨ Stylish Terminal UI: Enjoy a colorful, interactive CLI experience!
⚡ Easy Setup: Minimal installation steps to get you running in no time.
💻 Installation
📜 Requirements
Python 3.x (Make sure it's installed)
Termux (Perfect for Android users)
Mailgun API Key (Get your own from Mailgun)
🛠️ Installation Steps
Clone the repository:

First, clone the repository to your local machine:

git clone https://github.com/Lucifurge/PyeulMails-termuxOwn.git
Navigate into the project directory:


cd PyeulMails-termuxOwn
Install the required dependencies:

Run these commands to install all the necessary Python packages:


pip install requests     # For sending HTTP requests
pip install mailgun      # For Mailgun API integration
pip install colorama     # For beautiful terminal output
pip install pystyle      # For terminal style effects
🚀 Usage
📲 Running the Program
Once the installation is complete, run the script using:

bash
Copy
Edit
python mail.py
🧑‍💻 Available Options:
[1] Generate Mail: Generates a temporary email address and sends a test email.
[2] Exit: Exits the program.
💡 Tips:
Ensure you have your Mailgun API Key ready to configure the script for email sending/receiving.
Use Termux for an optimal experience on Android devices.
