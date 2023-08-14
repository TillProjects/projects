#!/usr/bin/env python3

import time
from playsound import playsound

# Definition der Klasse PomodoroTimer
class PomodoroTimer:
    # Initialisierungsfunktion
    def __init__(self, work_time, short_break_time, long_break_time, sound_file):
        # Umrechnung der Arbeits- und Pausenzeiten in Sekunden
        self.work_time = work_time * 60
        self.short_break_time = short_break_time * 60
        self.long_break_time = long_break_time * 60
        # Tondatei, die am Ende eines Timers abgespielt wird
        self.sound_file = sound_file

        # Anfangszählung der Runden
        self.rounds = 1

    # Funktion, um einen Timer zu starten und die verbleibende Zeit anzuzeigen
    def start_timer(self, seconds, timer_type):
        while seconds > 0:
            # Anzeige der verbleibenden Zeit
            print(f"\r{timer_type}: {seconds//60}:{seconds%60:02} min remaining",
                    end="")
            time.sleep(1)
            seconds -= 1
        if seconds == 0:
            print(f"\r{timer_type}: {seconds} seconds remaining", end="")
            # Abspielen der Tondatei, wenn der Timer abgelaufen ist
            playsound(self.sound_file)
            print(f"\n{timer_type} finished")

    # Funktion für den Arbeits-Timer
    def work(self):
        self.rounds += 1
        self.start_timer(self.work_time, 'Work time')

    # Funktion für die kurze Pause
    def short_break(self):
        self.start_timer(self.short_break_time, 'Short break')

    # Funktion für die lange Pause
    def long_break(self):
        self.start_timer(self.long_break_time, 'Long break')

    # Hauptfunktion, um den Pomodoro-Timer zu starten
    def start_pomodoro(self):
        try:
            while True:
                print('')
                # 4 Arbeitsintervalle und Pausen durchlaufen
                for i in range(4):
                    print(f'Round {self.rounds}')
                    self.work()
                    if i < 3:
                        self.short_break()
                    else:
                        # Nach 4 Arbeitsintervallen eine lange Pause
                        self.long_break()
                    print('')
        except KeyboardInterrupt:
            # Verarbeitet control + c, um Programm zu beenden
            print('')


if __name__ == "__main__":
    # Definiere die Zeiten für Arbeit, kurze und lange Pause
    work_time = 25
    short_break = 5
    long_break = 15
    # Erzeugt ein Objekt vom Typ PomodoroTimer
    timer = PomodoroTimer(work_time, short_break, long_break, 'lofi.mp3')
    # Startet den Pomodoro-Timer
    timer.start_pomodoro()
