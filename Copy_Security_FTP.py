import os
import shutil
import zipfile
from ftplib import FTP
import datetime

def copy_files(source_paths, temp_dir):
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    for source_path in source_paths:
        if os.path.exists(source_path):
            if os.path.isdir(source_path):
                shutil.copytree(source_path, temp_dir + '/' + os.path.basename(source_path))
            else:
                shutil.copy(source_path, temp_dir + '/' + os.path.basename(source_path))
        else:
            print('Path does not exist: ' + source_path)
    return temp_dir

def zip_files(temp_dir, backup_name):
    backup_zip = f"{backup_name}.zip"
    with zipfile.ZipFile(backup_zip, 'w') as zipf:
        for foldername, subfolders, filenames in os.walk(temp_dir):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                zipf.write(file_path, os.path.relpath(file_path, temp_dir))
    return backup_zip

def upload_to_ftp(ftp_host, ftp_user, ftp_password, zip_file, ftp_dir):
    try:
        with FTP(ftp_host) as ftp:
            ftp.login(ftp_user, ftp_password)
            ftp.cwd(ftp_dir)

            with open(zip_file, 'rb') as f:
                ftp.storbinary(f'STOR {os.path.basename(zip_file)}', f)

            print(f'File {zip_file} uploaded to FTP server')
    except Exception as e:
        print(f'Error uploading file to FTP server: {e}')

def main():
    source_paths = ['User/Example/Documents', 'User/Example/Pictures']
    temp_dir = 'User/Example/Temp'
    backup_name = f"Backup_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

    ftp_host = 'ftp.example.com'
    ftp_user = 'ftp_username'
    ftp_password = 'ftp_password'
    ftp_dir = '/backup'

    copy_files(source_paths, temp_dir)
    zip_file = zip_files(temp_dir, backup_name)
    print(f'Backup file created: {zip_file}')

    upload_to_ftp(ftp_host, ftp_user, ftp_password, zip_file, ftp_dir)

    shutil.rmtree(temp_dir)
    os.remove(zip_file)
   
if __name__ == '__main__':
    main()
    
