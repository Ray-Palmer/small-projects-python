import os
import shutil
import datetime
import schedule
import time


source_dir = ""
destination_dir = "D:/Backups"


def copy_folder_to_directory(source, destination):
    today = datetime.date.today()
    dest_dir = os.path.join(destination, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {destination}")


def main():
    schedule.every().day.at("12:00").do(
        lambda: copy_folder_to_directory(source_dir, destination_dir))

    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == '__main__':
    main()
