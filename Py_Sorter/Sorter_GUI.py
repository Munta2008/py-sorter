import customtkinter as ctk
from pathlib import Path

# Main window
app = ctk.CTk()
app.title("File Sorter App")
app.geometry("600x400")

# Entry box
entry = ctk.CTkEntry(app, placeholder_text="Enter folder path...")
entry.pack(pady=15)

# Log box (display area)
log_box = ctk.CTkTextbox(app, width=500, height=250)
log_box.pack(pady=10)
log_box.configure(state="disabled")


# Logging function
def log(message):
    log_box.configure(state="normal")
    log_box.insert("end", message + "\n")
    log_box.see("end")
    log_box.configure(state="disabled")


# Check/Create folders
def check_folder():
    log_box.configure(state="normal")
    log_box.delete("1.0", "end")
    log_box.configure(state="disabled")

    if not entry.get().strip():
        log("Please enter a folder path!")
        return

    directory = Path(entry.get())

    if not directory.exists():
        log("Base folder does not exist!")
        return

    # Define folders
    folders = {
        "Images": directory / "Images",
        "Texts": directory / "Texts",
        "Video": directory / "Video",
        "Audio": directory / "Audio",
        "Archive": directory / "Archive",
        "Other": directory / "Other"
    }

    # Check & create folders
    for name, folder in folders.items():
        if folder.exists():
            log(f"{name} folder found!")
        else:
            log(f"{name} folder not found. Creating...")
            folder.mkdir()
            log(f"{name} folder created.")


# Sort files
def sort_files():
    log_box.configure(state="normal")
    log_box.delete("1.0", "end")
    log_box.configure(state="disabled")

    if not entry.get().strip():
        log("Please enter a folder path!")
        return

    directory = Path(entry.get())

    if not directory.exists():
        log("Base folder does not exist!")
        return

    # Define folders
    image_file = directory / "Images"
    text_file = directory / "Texts"
    video_file = directory / "Video"
    audio_file = directory / "Audio"
    archive_file = directory / "Archive"
    other_file = directory / "Other"

    # Ensure folders exist
    for folder in [image_file, text_file, video_file, audio_file, archive_file, other_file]:
        folder.mkdir(exist_ok=True)

    # Sort files
    for file in directory.iterdir():
        if file.is_file():
            suffix = file.suffix.lower()

            try:
                if suffix in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']:
                    file.rename(image_file / file.name)
                    log(f"Moved {file.name} → Images")

                elif suffix in ['.txt', '.doc', '.docx', '.pdf', '.rtf']:
                    file.rename(text_file / file.name)
                    log(f"Moved {file.name} → Texts")

                elif suffix in ['.mp4', '.avi', '.mov', '.mkv', '.flv']:
                    file.rename(video_file / file.name)
                    log(f"Moved {file.name} → Video")

                elif suffix in ['.mp3', '.wav', '.aac', '.flac']:
                    file.rename(audio_file / file.name)
                    log(f"Moved {file.name} → Audio")

                elif suffix in ['.zip', '.rar', '.tar', '.gz']:
                    file.rename(archive_file / file.name)
                    log(f"Moved {file.name} → Archive")

                else:
                    file.rename(other_file / file.name)
                    log(f"Moved {file.name} → Other")

            except Exception as e:
                log(f"Error moving {file.name}: {e}")


# Buttons
check_folder_button = ctk.CTkButton(app, text="Check Folders", command=check_folder)
check_folder_button.pack(pady=5)

sort_files_button = ctk.CTkButton(app, text="Sort Files", command=sort_files)
sort_files_button.pack(pady=5)


# Run app
app.mainloop()