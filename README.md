# PyeulMails-termuxOwn ✨

Welcome to the **PyeulMails-termuxOwn** repository! 🎉 This is a **Termux-based tool** designed to generate temporary emails and interact with **Mailgun's API**. Whether you need a disposable email for testing or quick sign-ups, this tool has you covered. It also checks incoming emails for OTPs (One-Time Passwords) seamlessly!

---

![PyeulMails Logo](https://via.placeholder.com/150)

## 🚀 Features

- 🎯 **Random Temporary Email Generation**: Instantly create disposable email addresses with a click.
- 📧 **Mailgun Integration**: Send and receive emails using the **Mailgun API**.
- ✨ **Stylish Terminal UI**: Enjoy a colorful, interactive CLI experience!
- ⚡ **Easy Setup**: Minimal installation steps to get you running in no time.

---

## 💻 Installation

### 📜 Requirements

Make sure you have the following ready:

- **Python 3.x** (Make sure it's installed)
- **Termux** (Perfect for Android users)
- **Mailgun API Key** (Get your own from [Mailgun](https://www.mailgun.com/))

### 🛠️ Installation Steps

1. **Clone the repository:**

    First, clone the repository to your local machine:

    ```bash
    git clone https://github.com/Lucifurge/PyeulMails-termuxOwn.git
    ```

2. **Navigate into the project directory:**

    ```bash
    cd PyeulMails-termuxOwn
    ```

3. **Install the required dependencies:**

    Run these commands to install all the necessary Python packages:

    ```bash
    pip install requests     # For sending HTTP requests
    pip install mailgun      # For Mailgun API integration
    pip install colorama     # For beautiful terminal output
    pip install pystyle      # For terminal style effects
    ```

---

## 🚀 Usage

### 📲 Running the Program

Once the installation is complete, run the script using:

```bash
python mail.py
