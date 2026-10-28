import os
import shutil


folder_path = input("Enter the folder path to organize: ")

if not os.path.isdir(folder_path):
    print("Error: Folder not found!")

else:
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            extension = os.path.splitext(filename)[1].lower()

            if extension:
                folder_name = extension[1:].upper() + " Files"
                destination_folder = os.path.join(
                    folder_path, folder_name
                )

                os.makedirs(destination_folder, exist_ok=True)

                destination_path = os.path.join(
                    destination_folder, filename
                )

                if not os.path.exists(destination_path):
                    shutil.move(file_path, destination_path)
                    print("Moved:", filename)

    print("File organization completed!")
