from pathlib import Path

p = Path("C:\\Users\\munta\\Downloads") # Windows

# ------------------------------
# Variables for folder paths
# ------------------------------
image_file = p / "Images"
text_file = p / "Texts"
vedio_file = p / "Video"
audio_file = p / "Audio"
archive_file = p / "Archive"
other_file = p / "Other"


# ------------------------------
# Function to check and create folders
# ------------------------------
def check_folder(image_file, text_file, vedio_file, audio_file, archive_file, other_file):
    if image_file.exists() and image_file.is_dir():
        print("Image Folder found!")
    else:
        print("Image Folder not found.")
        image_file.mkdir()
        print("Image Folder created.")

    if text_file.exists() and text_file.is_dir():
        print("Text Folder found!")
    else:
        print("Text Folder not found.")
        text_file.mkdir()
        print("Text Folder created.")

    if vedio_file.exists() and vedio_file.is_dir():
        print("Video Folder found!")
    else:
        print("Video Folder not found.")
        vedio_file.mkdir()
        print("Video Folder created.")
        
    if audio_file.exists() and audio_file.is_dir():
        print("Audio Folder found!")
    else:
        print("Audio Folder not found.")
        audio_file.mkdir()
        print("Audio Folder created.")

    if archive_file.exists() and archive_file.is_dir():
        print("Archive Folder found!")
    else:
        print("Archive Folder not found.")
        archive_file.mkdir()
        print("Archive Folder created.")

    if other_file.exists() and other_file.is_dir():
        print("Other Folder found!")
    else:
        print("Other Folder not found.")
        other_file.mkdir()
        print("Other Folder created.")

# ------------------------------
# function to sort files 
# ------------------------------

def sort_files():
    for file in p.iterdir():
        if file.is_file():
            if file.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']:
                file.rename(image_file / file.name)
                print(f"Moved {file.name} to Images folder.")
            elif file.suffix.lower() in ['.txt', '.doc', '.docx', '.pdf', '.rtf']:
                file.rename(text_file / file.name)
                print(f"Moved {file.name} to Texts folder.")
            elif file.suffix.lower() in ['.mp4', '.avi', '.mov', '.mkv', '.flv']:
                file.rename(vedio_file / file.name)
                print(f"Moved {file.name} to Video folder.")
            elif file.suffix.lower() in ['.mp3', '.wav', '.aac', '.flac']:
                file.rename(audio_file / file.name)
                print(f"Moved {file.name} to Audio folder.")
            elif file.suffix.lower() in ['.zip', '.rar', '.tar', '.gz']:
                file.rename(archive_file / file.name)
            else:
                file.rename(other_file / file.name)

# ------------------------------
# Main Execution
# ------------------------------
check_folder(image_file, text_file, vedio_file, audio_file, archive_file, other_file)
sort_files()