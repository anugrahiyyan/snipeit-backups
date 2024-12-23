# SnipeIT-Backup Console

Welcome to the **SnipeIT-Backup Console**, a Python-based interactive script for securely downloading backup files from a remote SFTP server. This program comes with a colorful interface, ASCII art, and smooth animations to enhance the user experience.

## Features
- Securely connect to a remote SFTP server using SSH.
- List available `.zip` backup files from a specified remote directory.
- Download selected files with a real-time progress bar.
- Interactive interface with options to perform multiple downloads.
- Animated farewell message when exiting.

## Prerequisites
- Python 3.8 or higher.
- A working SSH server with the following:
  - Host IP
  - Username and Password
- Write permissions for the specified local directory to store the backups.

## Installation Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/anugrahiyyan/snipeit-backups.git
   cd snipeit-backups
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the program:
   ```bash
   python Click_Me_To_Backup_SnipeIT.py
   ```

## Usage
1. Launch the script and enter your SSH credentials when prompted.
2. View the list of available `.zip` backup files.
3. Select a file by entering its corresponding number.
4. Enjoy the progress bar as the file downloads.
5. After the download completes, choose whether to download another file or exit.
6. If you exit, watch the animated farewell message!

## Example Output
Upon running the program, you will see:
```plaintext
  _____       _             ______  ______            _                  
 / ____|     (_)           |  ____|/ ____|          | |                 
| (___   _ __ _ _ __   __ _| |__  | (___   ___   ___| |_ ___  _ __ ___  
 \___ \ | '__| | '_ \ / _` |  __|  \___ \ / _ \ / __| __/ _ \| '__/ __|
 ____) || |  | | | | | (_| | |____ ____) | (_) | (__| || (_) | |  \__ \
|_____/ |_|  |_|_| |_|\__, |______|_____/ \___/ \___|\__\___/|_|  |___/
                      __/ |                                            
                     |___/                                             

Welcome to SnipeIT-Backup Console, created by Galbatorix

Please enter your credentials to continue...
```

## License
This project is licensed under the MIT License. Feel free to modify and share!

## Author
Created by **Galbatorix**.
