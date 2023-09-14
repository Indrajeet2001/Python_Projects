import os
import shutil

# Define the source directory where unorganized files are located
source_dir = "C:/Users/Lenovo/Desktop/LB_Python/FIle_Handling"

# Create a dictionary with file types as keys and corresponding folders as values
file_types = {
    "Documents": [".pdf", ".docx", ".txt"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar.gz"],
    "Others": []  # Default folder for other file types
}

# Create destination folders if they don't exist
for folder in file_types.keys():
    folder_path = os.path.join(source_dir, folder)
    os.makedirs(folder_path, exist_ok=True)

# Loop through files in the source directory
for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)

    # Check if it's a file (not a folder)
    if os.path.isfile(file_path):
        # Get the file extension (e.g., ".pdf")
        file_extension = os.path.splitext(filename)[1]

        # Find the folder corresponding to the file type
        destination_folder = None
        for folder, extensions in file_types.items():
            if file_extension.lower() in extensions:
                destination_folder = folder
                break

        # If no specific folder is found, place the file in the "Others" folder
        if destination_folder is None:
            destination_folder = "Others"

        # Construct the destination path
        destination_path = os.path.join(source_dir, destination_folder, filename)

        # Move or copy the file to the destination folder
        shutil.move(file_path, destination_path)  # Use shutil.copy for copying instead

print("File organization complete.")
