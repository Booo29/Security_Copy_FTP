# Security_Copy_FTP

This Python script automates the process of creating a backup of files or directories, compressing them into a ZIP file, and uploading the backup to an FTP server. After uploading, the temporary files and directories are deleted.

## Features
- **Copies files and directories to a temporary directory.**
- **Compresses the copied files into a ZIP file.**
- **Uploads the ZIP file to a specified FTP server.**
- **Cleans up the temporary files and the backup ZIP file after uploading.**

## How to Use

Clone or download the script.

Modify the following variables in the main() function to match your paths and FTP credentials:

- **source_paths:** A list of file or directory paths you want to back up.
- **temp_dir:** A temporary directory where the files will be copied before zipping.
- **ftp_host:** The address of your FTP server.
- **ftp_user:** Your FTP username.
- **ftp_password:** Your FTP password.
- **ftp_dir:** The directory on the FTP server where the ZIP file will be uploaded.

## Notes
- **The backup ZIP file will be named Backup_YYYY-MM-DD_HH-MM-SS.zip, with the current date and time included.**
- **The script automatically deletes the temporary directory and ZIP file after uploading to free up space.**
- **Ensure your FTP credentials are correct and you have the necessary permissions to upload to the FTP server.**
