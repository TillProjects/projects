#!/usr/bin/env python3
# stopwatch.py - A simple stopwatch program.

import time

# Display the program's instructions.
print('Press enter to begin. Afterwards, press ENTER to "click" the stopwatch. '
      'Press Ctrl-C to quit.', end='')
input()  # press Enter to begin
print('Started.', end='\n\n\n')
startTime = time.time()  # get the first lap's start time
lastTime = startTime
lapNum = 1

# Start tracking the lap times.
try:
    print('Lap Number\tTotal Time\tLap Time', end='')
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print(f'#{lapNum}\t{totalTime}\t({lapTime})', end='')
        lapNum += 1
        lastTime = time.time()  # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    lapTime = round(time.time() - lastTime, 2)
    totalTime = round(time.time() - startTime, 2)
    print(f'\n#{lapNum}\t{totalTime}\t({lapTime})')
    print(f'Total Time: {totalTime}')
    print('\nDone.')
