from pathlib import Path
import shutil

selected_folder = Path(input("Enter folder path: "))
folder_type = [
    {
        "folderName" : "Images",
        "folderType" : [".png",".jpeg",".jpg"]
    },
    {
        "folderName" : "Videos",
        "folderType" : [".mp4",".mov",".avi",".mkv",".webm"]
    },
    {
        "folderName" : "Documents",
        "folderType" : [".docx",".txt"]
    },
]

if not selected_folder.exists():
    print("Selected folder does not exist")

else:
    skip_files=0
    for entry in selected_folder.iterdir():
        if entry.is_file():
            file_extension_type = entry.suffix.lower()
            folderName = "Others"
            

            if file_extension_type=="":
                skip_files +=1
                continue

            for category in folder_type:
                if file_extension_type in category["folderType"]:
                    folderName = category["folderName"]
                    break
                
            transfer_dir = selected_folder / folderName

            transfer_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(entry, transfer_dir)

    print(f"Skipped files: {skip_files}")
