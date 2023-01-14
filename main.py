import tkinter
import customtkinter as ctk
from pytube import YouTube
import math

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("720x480")
app.title("Youtube Video Downloader")


def download():
    if link != "":
        link_to_download = yt_link
        yt = YouTube(link_to_download.get(), on_progress_callback=progress)
        stream = yt.streams.get_highest_resolution()
        stream.download()
    else:
        text.configure("Enter a valid link!")
    text.configure("Downloaded!!!")


def progress(stream, chunk, bytes_remaining):
    file_size = stream.filesize
    bytes_downloaded = file_size - bytes_remaining
    percentage = (bytes_downloaded / file_size) * 100
    progress_label.configure(text=f"{math.floor(percentage):.0f}%")
    progressBar.set(math.floor(percentage))
    print(math.floor(percentage))


label = ctk.CTkLabel(
    master=app, text="Enter youtube link", font=("Ubuntu", 20))
label.pack(padx=20, pady=20)


yt_link = tkinter.StringVar()
link = ctk.CTkEntry(
    master=app, width=400, height=30, textvariable=yt_link)
link.pack(padx=10, pady=10)

download_btn = ctk.CTkButton(
    master=app, text="Download", command=download)
download_btn.pack(pady=10)

progress_label = ctk.CTkLabel(master=app, text="0%")
progress_label.pack(pady=10)

progressBar = ctk.CTkProgressBar(master=app)
progressBar.set(0)
progressBar.pack(pady=10)

text = ctk.CTkLabel(master=app, text="")
text.pack()

app.mainloop()
