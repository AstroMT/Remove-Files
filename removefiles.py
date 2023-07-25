import time
import os
import shutil


path = input("Enter the path: ") 
days = int(input("Enter the number of days: "))

delete_old_files(path, days)


def delete_old_files(path, days):
    seconds = days * 24 * 60 * 60

    if os.path.exists(path) == True:
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                ctime = os.stat(file_path).st_ctime
                if (time.time() - ctime) > seconds:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                        print("Deleted file: ", file_path)
                    else:
                        shutil.rmtree(file_path)
                        print("Deleted folder: ", file_path)
                else:
                    print("No files/folders available.")
    else:
        print("Path not found.")