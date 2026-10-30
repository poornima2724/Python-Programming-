import os
import shutil

source = input("Enter source folder path: ")
destination = input("Enter destination folder path: ")

if not os.path.isdir(source):
    print("Source folder does not exist!")

elif os.path.abspath(source) == os.path.abspath(destination):
    print("Source and destination folders must be different!")

else:
    os.makedirs(destination, exist_ok=True)

    count = 0

    for file in os.listdir(source):
        if file.lower().endswith(".jpg"):
            source_path = os.path.join(source, file)
            destination_path = os.path.join(destination, file)

            if os.path.isfile(source_path):
                shutil.move(source_path, destination_path)
                count += 1

    print(count, "JPG files moved successfully!")
