#!/usr/bin/env python3
# YouTube Video URL kopieren, durch rechtsklick auf Video.
# Dann ./youtube_downloader.py URL

from pytube import YouTube
from sys import argv

url = argv[1]
yt = YouTube(url)

# Wählt den Stream mit der höchsten Auflösung aus
stream = yt.streams.get_highest_resolution()

# Lädt das Video herunter
stream.download('/Users/till/Documents/YouTube/')
