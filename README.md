FILE ORGANIZER CLI

A lightweight Python script that automatically cleans up and organizes messy directories by sorting files into categorized subfolders based on their extensions.

FEATURES

Automatic Categorization: Groups files into Images, Videos, Documents, and defaults unlisted types to Others.
Built-in Safety Checks: Validates input paths and gracefully handles files without extensions.
Zero External Dependencies: Uses only Python's built-in pathlib and shutil modules.
Execution Summary: Reports the total count of successfully organized files and skipped items.

SUPPORTED CATEGORIES

Images:    .png, .jpeg, .jpg, .gif 

Videos:    .mp4, .mov, .avi, .mkv, .webm 

Documents: .docx, .txt 

Audio:     .mp3, .wav, .flac 

Others:    Any other unlisted extension 


HOW TO USE

Clone or download the script (e.g., organizer.py) to your local machine.
Open your terminal or command prompt.
Run the script using Python:
python organizer.py
Enter the absolute or relative path of the directory you want to organize when prompted.
