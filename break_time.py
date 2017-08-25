import time
import webbrowser


totalBreaks = 3
breaksTaken = 0
print("This program started on" + time.ctime())
while (breaksTaken < totalBreaks):
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=H4o5tGajfYE")
    breaksTaken += 1
