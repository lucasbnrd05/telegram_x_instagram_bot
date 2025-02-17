# ⚠️ Warning

This project is provided for educational purposes only. The author disclaims any responsibility for misuse of this tool. It is strongly advised not to use photos that do not belong to you. Please adhere to the laws and privacy regulations in force.

# 📌 Project Overview

This project was developed to enhance my skills in Python and API integration. It allows you to:

- ✅ Download photos from Instagram 📸
- ✅ Apply deepfake technology to these images using the Roop GitHub repo 🤖
- ✅ Automatically post the modified images on Instagram 📤
- ✅ Control the entire process via a Telegram bot 🤖📱

The GitHub repository for Roop is included in this project folder.

This project centralizes all these features in one place, making it easier to manage automated content.

## 🔴 Warning: 
Using this project for malicious or unethical actions is strongly discouraged and may violate Instagram's terms of service and other platforms' regulations.

# 🛠️ Installation and Setup

# Project Setup Guide

This guide will walk you through the installation process and setup for running the project. The instructions are divided based on your platform (Linux, MacOS, Windows).

---

## 1. Setup Your Platform

### Linux

1. **Install Python**  
   ```bash
   sudo apt install python3.10
   ```

2. **Install PIP**  
   ```bash
   sudo apt install python3-pip
   ```

3. **Install GIT**  
   ```bash
   sudo apt install git-all
   ```

4. **Install FFmpeg**  
   ```bash
   sudo apt install ffmpeg
   ```

### MacOS

1. **Install Python**  
   ```bash
   brew install python@3.10
   ```

2. **Install PIP**  
   ```bash
   python -m ensurepip
   ```

3. **Install GIT**  
   ```bash
   brew install git
   ```

4. **Install FFmpeg**  
   ```bash
   brew install ffmpeg
   ```

### Windows

*Currently, there is no official support for Windows. The setup guide is focused on Linux and MacOS for now.*

---

## 2. Clone Repository

To get started, clone the GitHub repository to your local machine:

```bash
git clone https://github.com/lucasbnrd05/telegram_x_instagram_bot
```

Navigate to the folder where the repository is cloned:

```bash
cd telegram_x_instagram_bot
git submodule update --init --recursive
```
This allows Git to read the information in the .gitmodules file and fetch the content of the specified submodules, ensuring that all required submodules are downloaded and correctly integrated into your project.

---

If the above command doesn't work, you can manually clone the submodule directly to the root of the project by running the following command:

```bash
git clone https://github.com/s0md3v/roop
```

This will fetch the submodule content directly and integrate it into the project.

## 3. Install Dependencies

We highly recommend using a **virtual environment (venv)** or **conda** to avoid potential issues with system-wide packages.

### Using a Virtual Environment (venv)

1. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

2. Activate the virtual environment:

   **Linux/MacOS:**
   ```bash
   source venv/bin/activate
   ```

   **Windows:**
   ```bash
   .\venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## 4. Setup Telegram Bot

To control the entire process via Telegram, you'll need to create a Telegram bot. Follow these steps:

1. Open **Telegram** and search for the **BotFather** bot.

2. Start a chat with BotFather and follow the instructions to create a new bot. You will receive a **Bot Token**.

3. Save the **Bot Token** for later use.

4. In the project folder, open the `run_bot.py` file.

5. On **line 11**, you’ll find the following line:

   ```python
   telegram_api_key = "Your Telegram Key"
    ```

6. Replace "Your Telegram Key" with the token you received from BotFather:
    ```python
    telegram_api_key = "YourActualTelegramTokenHere"
    ```

---

## 5. Configure Instagram 

To download and post images to Instagram automatically, you’ll need to configure the Instagram login in the script.

1. In the project folder, open the relevant Python script (likely `run_bot.py` or a similar file).

2. On **line 30**, you’ll find the following line:

   ```python
   cl.login("Your instagram name", "Your instagram password")
   ```

3. Replace `"Your instagram name"` and `"Your instagram password"` with your actual Instagram credentials:

   ```python
   cl.login("YourActualInstagramUsername", "YourActualInstagramPassword")
   ```

4. On **line 102**, you’ll find a command like this:

   ```python
   os.system(f"python3 -m instaloader --login 'Your instagram login' +args.txt {string_ref}")
   ```

5. Replace `'Your instagram login'` with your Instagram username:

   ```python
   os.system(f"python3 -m instaloader --login 'YourInstagramUsername' +args.txt {string_ref}")
   ```

---

## 6. Upload Image for Deepfake

Before running the script, you need to provide a `.png` image of the person you want to use for the deepfake process.

1. The image should be in **square format** (e.g., 512x512, 1024x1024, etc.) for best results.

2. The image should be placed at the **root directory** of the project.

3. Name the image file appropriately, such as `ref.png`.

Now the script will use this image for processing.



## 7. Run the Project

Once everything is set up:

1. **Activate the virtual environment** (if you haven't already).

2. Run the main Python script to start the bot and begin the image modification process:

   ```bash
   python run_bot.py
   ```
3. Instagram Login Prompt:
On the first launch, you may be asked for your Instagram account password in the terminal. This is due to the login process where the script authenticates with Instagram for the first time. Once the login is completed, the credentials might be cached, and you won't need to enter your password in subsequent runs.

   Follow the on-screen instructions to control the bot via Telegram.

---

## How to Use on Telegram

To use the bot, it's recommended to run it on a **server** for continuous operation. However, if you don't have a server, you can also run it directly from your terminal.

### 1. Launch the Bot

1. **Activate the virtual environment** (if you haven't already).

2. Run the bot with the following command:

   ```bash
   python run_bot.py
   ```

3. Once the bot is running, open **Telegram** and search for your bot.

4. Start a conversation with the bot and type the following command:

   ```
   /start
   ```

   This will trigger the bot and display the list of available commands.

### 2. List of Available Commands

Here is the list of commands you can use in the bot:

- `/Set_`: Defines the list of accounts to take content from.
- `/List_`: Returns the list if filled, otherwise returns an empty list.
- `/Import_`: Imports a new model.
- `/Faceswap_`: Faceswap model.
- `/Publication_`: Publishes every 6 hours.
- `/Stoppubli_`: Stops publishing.
- `/Like_`: Likes posts based on defined hashtags.
- `/Comment_`: Comments on posts based on hashtags.
- `/LikeComment_`: Likes and comments on posts based on hashtags.
- `/AjoutHtag_`: Adds a hashtag.
- `/SupHtag_`: Removes a hashtag.
- `/EnumHtag_`: Returns the list of hashtags if filled, otherwise returns an empty list.
- `/Listemessage_`: Returns the list of unread messages.
- `/Respons_`: Allows replying to one or more users with the desired message. (Format: `Respons_user_textresponse,user_textresponse...`)

Once you've launched the bot, you can use these commands to control its behavior via Telegram.
