import customtkinter as ctk
from pathlib import Path
import time

# Main application window
app = ctk.CTk()
app.title("Path Storage App")
app.geometry("400x200")
entry = ctk.CTkEntry(app, placeholder_text="Type something...")
entry.pack(pady=20)


p = None 

def save_path():
    global p 
    directory = Path(entry.get())
    p = Path(directory)
    print("Stored path:", p)

if p is not None:
    image_file = p / "Images"
    text_file = p / "Texts"
    video_file = p / "Video"
    audio_file = p / "Audio"
    archive_file = p / "Archive"
    other_file = p / "Other"

submit = ctk.CTkButton(app, text="Submit", command=save_path)
submit.pack(pady=10)

app.mainloop()