from ftplib import FTP

HOST = "ftp.example.com"
USERNAME = "your_username"
PASSWORD = "your_password"

with FTP(HOST) as ftp:
    ftp.login(user=USERNAME, passwd=PASSWORD)
    print(f"Connected to FTP server: {HOST}")

    # List files in the current directory
    files = ftp.nlst()
    print("Files in the current directory:")
    for file in files:
        print(file)

    # Upload a file
    filename = "example.txt"
    with open(filename, "rb") as file:
        ftp.storbinary(f"STOR {filename}", file)
        print(f"Uploaded {filename} to the FTP server.")

    # Download a file
    download_filename = "downloaded_example.txt"
    with open(download_filename, "wb") as file:
        ftp.retrbinary(f"RETR {filename}", file.write)
        print(f"Downloaded {filename} as {download_filename}.")

    # Close the connection
    ftp.quit()
    print("FTP session closed.")