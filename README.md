FILE ORGANIZER CLI

A lightweight Python script that automatically cleans up and organizes messy directories by sorting files into categorized subfolders based on their extensions.

FEATURES

Automatic Categorization: Groups files into Images, Videos, Documents, and defaults unlisted types to Others.
Built-in Safety Checks: Validates input paths and gracefully handles files without extensions.
Zero External Dependencies: Uses only Python's built-in pathlib and shutil modules.
Execution Summary: Reports the total count of successfully organized files and skipped items.

SUPPORTED CATEGORIES

Images:    .png, .jpeg, .jpg, .gif \n
Videos:    .mp4, .mov, .avi, .mkv, .webm \n
Documents: .docx, .txt \n
Audio:     .mp3, .wav, .flac \n
Others:    Any other unlisted extension \n

HOW TO USE

Clone or download the script (e.g., organizer.py) to your local machine.
Open your terminal or command prompt.
Run the script using Python:
python organizer.py
Enter the absolute or relative path of the directory you want to organize when prompted.

CUSTOMIZATION

You can easily modify or expand the categories and file types by updating the folder_type list at the top of the script:
folder_type = [
{
"folderName": "Images",
"folderType": [".png", ".jpeg", ".jpg", ".gif"]  # Added .gif example
},
# Add new categories here
]
