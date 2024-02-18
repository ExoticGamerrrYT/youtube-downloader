import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=onProgress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
        finish_lbl.configure(text="")

        video.download()
        finish_lbl.configure(text="Downloaded!", text_color="white")
    except:
       finish_lbl.configure(text="YouTube link is invalid.", text_color="red")
    

def onProgress(stream, chunk, bytesRemaining):
    totalSize = stream.filesize
    bytesDownloaded = totalSize - bytesRemaining
    percentageOfCompletion = bytesDownloaded / totalSize * 100
    #print(percentageOfCompletion)
    per = str(int(percentageOfCompletion))
    pPercentage.configure(text=per + "%")
    pPercentage.update()

    # Update Progressbar
    progressBar.set(float(percentageOfCompletion) / 100)


# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.wm_geometry("720x480")
app.wm_title("YouTube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finish downloading
finish_lbl = customtkinter.CTkLabel(app, text="")
finish_lbl.pack()

# Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Run app
app.mainloop()