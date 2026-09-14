from pathlib import Path
import shutil

folder_type = [
            {
                "folderName" : "Images",
                "folderType" : [".png",".jpeg",".jpg",".gif"]
            },
            {
                "folderName" : "Videos",
                "folderType" : [".mp4",".mov",".avi",".mkv",".webm"]
            },
            {
                "folderName" : "Documents",
                "folderType" : [".docx",".txt"]
            },
            {
                "folderName" : "Audio",
                "folderType" : [".mp3",".wav",".flac"]
            }
        ]

def get_folder():
    s=input("Enter folder path: ")
    folder_path = Path(s)
    if not folder_path.exists() or not folder_path.is_dir():
        return 
    return folder_path

def get_extension(item):
    return item.suffix.lower()

def get_category(file_extension):
    for category in folder_type:
        if file_extension in category["folderType"]:
            return category["folderName"]
    return "Others"

def move_file(curr_file,dir_folder):
    dir_folder.mkdir(parents=True, exist_ok=True)
    shutil.move(curr_file,dir_folder)

def main():

    skipped_file=0
    file_organised=0

    selected_folder=get_folder()
    if selected_folder is not None:
        for item in selected_folder.iterdir():
            if item.is_file():

                file_extension = get_extension(item)
                if file_extension=="":
                    skipped_file +=1
                    continue

                file_category = get_category(file_extension)
                dir_folder = selected_folder/file_category
                move_file(item,dir_folder)
                file_organised +=1
    else:
        print("Input Path does not exist")

    print("Files Organised :",file_organised)
    print("Skipped Files :",skipped_file)
main()