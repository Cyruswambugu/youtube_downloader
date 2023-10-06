import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
from pytube.exceptions import VideoUnavailable
import os

# Function to download the video
def download_video():
    try:
        # Get the URL and output directory from the GUI
        video_url = url_entry.get()
        output_directory = directory_entry.get()

        # Create a YouTube object
        yt = YouTube(video_url)

        # Choose the stream you want to download (e.g., highest resolution video)
        stream = yt.streams.get_highest_resolution()

        # Create the output directory if it doesn't exist
        os.makedirs(output_directory, exist_ok=True)

        # Download the video to the specified directory
        stream.download(output_path=output_directory)

        status_label.config(text="Video downloaded successfully!")

    except VideoUnavailable:
        status_label.config(text="Error: The video is unavailable or the URL is invalid.")
    except Exception as e:
        status_label.config(text=f"An error occurred: {e}")

# Create the main GUI window
window = tk.Tk()
window.title("YouTube Video Downloader")

# Create URL input label and entry field
url_label = tk.Label(window, text="Enter YouTube Video URL:")
url_label.pack()
url_entry = tk.Entry(window, width=50)
url_entry.pack()

# Create output directory input label and entry field
directory_label = tk.Label(window, text="Choose Output Directory:")
directory_label.pack()
directory_entry = tk.Entry(window, width=50)
directory_entry.pack()

# Create a button to start the download
download_button = tk.Button(window, text="Download Video", command=download_video)
download_button.pack()

# Create a label to display download status
status_label = tk.Label(window, text="")
status_label.pack()

# Start the GUI event loop
window.mainloop()










