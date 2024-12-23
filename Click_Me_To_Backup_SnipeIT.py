import paramiko
import getpass
from tqdm import tqdm
import os
import pyfiglet
from colorama import Fore, Style, init
import time
import itertools

# Initialize colorama
init(autoreset=True)

# SSH connection details
host = "192.168.xx.xxx"
port = 22
username = "your_username"
remote_path = "/var/www/html/snipeit/storage/app/backups/" # Change if the locations different.
local_path = r"C:\Users\your_path" # Use Your Local Folder or whatever.

def display_exit_animation():
    """Displays a farewell message and a train animation."""
    print(Fore.CYAN + "\nBye Bye Big Boss. See you next week!\n")
    
    # Simple train animation
    train = [
        "🚂💨      ",
        "   🚂💨   ",
        "      🚂💨"
    ]
    for _ in range(10):  # Loop for animation
        for frame in train:
            print(Fore.GREEN + f"\r{frame}", end="")
            time.sleep(0.3)
    print("\n")

def download_file():
    """Handles the file downloading process."""
    try:
        # Establish SSH connection
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password)

        # Use SFTP to list files
        sftp = ssh.open_sftp()
        files = sftp.listdir(remote_path)

        zip_files = [file for file in files if file.endswith(".zip")]

        if not zip_files:
            print(Fore.RED + f"No .zip files found in {remote_path}. Exiting.")
            return False
        else:
            # Display only the filenames, excluding the full path
            print(Fore.GREEN + "\nAvailable backup files:")
            for idx, filename in enumerate(zip_files, start=1):
                print(Fore.WHITE + f"{idx}. {filename}")

            while True:
                # Prompt user to select a file
                file_choice = input(Fore.YELLOW + "Enter the number of the file you want to download (or type 'exit' to quit): ").strip()

                if file_choice.lower() == "exit":
                    display_exit_animation()
                    return False  # Stop the loop and exit the program

                if not file_choice.isdigit() or not (1 <= int(file_choice) <= len(zip_files)):
                    print(Fore.RED + "Are you blind or what?. Please enter a valid backups file number!!.")
                else:
                    selected_file = zip_files[int(file_choice) - 1]

                    # Ensure the local directory exists
                    os.makedirs(local_path, exist_ok=True)
                    local_file_path = os.path.join(local_path, selected_file)

                    # Open the file and get its size
                    remote_file_path = remote_path + selected_file
                    file_size = sftp.stat(remote_file_path).st_size

                    # Use tqdm to display progress manually
                    print(Fore.CYAN + f"\nDownloading {selected_file} to this secure machine ...")
                    print(Fore.CYAN + f"Ngopi Dulu Ga Sih ...\n")

                    with tqdm(total=file_size, unit='B', unit_scale=True, desc=f"Downloading {selected_file}") as progress_bar:
                        with open(local_file_path, 'wb') as local_file:
                            # Read the file in chunks and update progress
                            with sftp.open(remote_file_path, 'rb') as remote_file:
                                while True:
                                    data = remote_file.read(1024 * 1024)  # Read in 1MB chunks
                                    if not data:
                                        break
                                    local_file.write(data)
                                    progress_bar.update(len(data))

                    print(Fore.GREEN + f"\nFile downloaded successfully to {local_file_path}!")
                    return True

    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")
        return False
    finally:
        if 'sftp' in locals():
            sftp.close()
        if 'ssh' in locals():
            ssh.close()

# Display ASCII Art Welcome Message
ascii_art = pyfiglet.figlet_format("SnipeIT-Backup")
print(Fore.GREEN + ascii_art)
print(Fore.CYAN + "Welcome to SnipeIT-Backup Console, created by Galbatorix\n")
print(Fore.YELLOW + "Please enter your credentials to continue...\n")

# Prompt for SSH password
password = getpass.getpass(Fore.YELLOW + "Credentials: ")

# Interactive loop
while True:
    if download_file():
        user_input = input(Fore.YELLOW + "\nYour download is done, sir! Would you like to stay here? (Y/N): ").strip().upper()
        if user_input == "N":
            display_exit_animation()
            break
        elif user_input != "Y":
            print(Fore.RED + "Invalid choice. Assuming you want to stay.")
    else:
        break
