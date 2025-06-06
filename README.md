# Discord Spammer GUI

A Python-based GUI application for automating messages in a specific Discord channel, built with Tkinter and Selenium. The application provides a simple user interface to log in, target a channel, and send a message repeatedly.

## Showcase
[![Watch the video](https://i9.ytimg.com/vi/HM5oZzbomzQ/mqdefault.jpg?sqp=CPTAi8IG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGCMgEyh_MA8=&rs=AOn4CLATAFWfLLk0ebHH3LnjzO_LrYwPZg)](https://www.youtube.com/watch?v=HM5oZzbomzQ&ab_channel=LucajDev)

## ⚠️ Disclaimer

This tool is intended for **educational purposes ONLY**. Automating user accounts and sending spam messages is a direct violation of Discord's [Terms of Service](https://discord.com/terms). Using this tool can result in the temporary or permanent suspension of your Discord account. The creator of this script is not responsible for any actions you take or any consequences that may arise from its use. **Use at your own risk.**

## Features

- **User-Friendly Interface:** A simple GUI built with Tkinter, featuring a custom background.
- **Secure Credentials:** Loads your Discord username and password securely from a local `.env` file, keeping them out of the source code.
- **Full Automation:** Automates the entire process:
    - Logs into Discord.
    - Navigates to the specified server.
    - Selects the specified channel.
    - Sends the user-defined message.
- **Real-Time Feedback:** An embedded console output window shows the script's progress and status in real-time.
- **Safe from Freezing:** The automation process runs in a separate thread to ensure the GUI remains responsive at all times.

## Setup & Installation

Follow these steps to get the application running on your local machine.

### Prerequisites

- Python 3.x
- Google Chrome browser installed on your system.

### 1. Clone the Repository

First, clone this repository to your local machine or download the source code as a ZIP file.

```bash
git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
cd your-repository-name 
```

### 2. Install Dependencies
Install all the required Python libraries using pip. It's recommended to do this within a virtual environment.
```bash
pip install -r requirements.txt
```
If you don't have a `requirements.txt` file, you can install the libraries manually:
```bash
pip install selenium python-dotenv webdriver-manager Pillow
```

### 3. Create the `.env` File
Create a file named `.env` in the root directory of the project. This file will store your login credentials. Add your Discord email and password to this file as follows:
```bash
USERNAME=your.email@example.com
PASSWORD=YourPassword
```
## How to Use
1.  **Run the Application:**
    Start the GUI by running the `gui_main.py` script.
    ```
    python gui_main.py
    ```

2.  **Find Your Server and Channel ID:**
    To get the IDs, you must first enable **Developer Mode** in Discord.
    - Go to `User Settings` > `Advanced`.
    - Toggle `Developer Mode` on.
    - Now, you can right-click on any server icon or channel name and select **"Copy Server ID"** or **"Copy Channel ID"**.

3.  **Fill in the Fields:**
    - **Server ID:** Paste the copied Server ID.
    - **Channel ID:** Paste the copied Channel ID.
    - **Message:** Type the message you want to send.

4.  **Start Spamming:**
    - Click the **"Spam Now"** button.
    - A new Chrome window will open and begin the automation process. You can monitor the progress in the application's output console.
    - The process will run until it is stopped or the browser window is closed.

