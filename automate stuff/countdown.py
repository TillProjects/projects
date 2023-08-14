#!/usr/bin/env python3
# countdown.py - Ein einfaches Countdown-Skript

from sys import argv
import time
from playsound import playsound

# import subprocess

if argv == 2:
    timeLeft = int(argv[1])
else:
    timeLeft = 2

# sound_pfad = '/Users/till/Documents/git/pyCharm/automatisieren/lofi.mp3'
while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft -= 1

playsound('lofi.mp3')
# subprocess.Popen(['open', sound_pfad])
