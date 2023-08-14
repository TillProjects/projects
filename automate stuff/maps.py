#!/usr/bin/env python3
# maps.py - öffnet im Browser eine Karte zu der Anschrift in der
# Befehlszeile oder Zwischenablage
# mit den Parameter -s wird nach einem Ort gesucht

import webbrowser
import argparse
import pyperclip


def open_address(place):
    webbrowser.open(f'https://www.google.de/maps/place/{place}')


def search_address(place):
    webbrowser.open(f'https://www.google.de/maps/search/{place}')


def parse_command_line():
    # Erzeugt den ArgumentParser
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--search', action='store_true',
                        help='Sucht nach dem Ort/ Platz.')
    parser.add_argument('address', nargs='*',
                        help='Die Adresse, die geöffnet werden soll.')
    return parser.parse_args()


args = parse_command_line()

# Bestimmt die Adresse aus den Befehlszeilenargumenten oder aus der
# Zwischenablage
address = '+'.join(args.address) if args.address else pyperclip.paste()

# Ruft die entsprechende Funktion auf, abhängig von der Option -s/--search
if args.search:
    search_address(address)
else:
    open_address(address)
