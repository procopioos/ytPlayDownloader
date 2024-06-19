from bs4 import BeautifulSoup
import requests
import os
from pytube import YouTube
from pytube import Playlist as PyTubePlaylist
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory

class Playlist:
    def __init__(self, playListUrl):
        self.playListUrl = playListUrl
        self.videos = self.get_playlist_videos()
        self.download_videos()

    def get_playlist_videos(self):
        playlist = PyTubePlaylist(self.playListUrl)
        return playlist.video_urls

    def download_videos(self):
        fwrite = open("playlist_detail.txt", "a")  # Writing all songs from the Playlist on a text file
        for i, url in enumerate(self.videos):
            try:
                global yt
                yt = YouTube(url)
                video = yt.streams.get_highest_resolution()
                print(f"Downloading: {yt.title} in {destination}")
                video.download(f"{destination}")
                print(f"Downloaded: {yt.title}")
            except Exception as e:
                print(f"Error downloading video {i+1}: {e}")
        fwrite.close()

def chooseLoc():
    global destination
    destination = askdirectory()

def dwnload():
    url = urlTxt.get("1.0", tk.END).strip()
    if url:
        Playlist(url)

if __name__ == "__main__":
    print("        _   _____  _             _____                      _                 _           ")
    print("       | | |  __ \| |           |  __ \                    | |               | |          ")
    print("  _   _| |_| |__) | | __ _ _   _| |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __ ")
    print(" | | | | __|  ___/| |/ _` | | | | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|")
    print(" | |_| | |_| |    | | (_| | |_| | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   ")
    print("  \__, |\__|_|    |_|\__,_|\__, |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   ")
    print("   __/ |                    __/ |                                                         ")
    print("  |___/                    |___/                                                  v1.0-GUI")

    root = tk.Tk()
    root.geometry("380x170")
    root.resizable(False, False)
    root.title("ytPlayDownloader-GUI")
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="URL:").grid(column=0, row=0, sticky='W')
    urlTxt = tk.Text(frm, height=1, width=30)
    urlTxt.grid(column=0, row=1, sticky='W')
    ttk.Label(frm, text="Destination folder:").grid(column=1, row=0, sticky='E', padx=10)
    DestBTN = tk.Button(frm, text="Choose...", command=chooseLoc)
    DestBTN.grid(column=1, row=1, sticky='E', padx=10)
    DwnloadBTN = tk.Button(frm, text="Start download", command=dwnload)
    DwnloadBTN.grid(column=0, row=2, sticky='W')
    root.mainloop()