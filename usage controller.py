import time
import os
from plyer import notification

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=20 # Reduced timeout to avoid long interruptions
    )

counter_hour = 0
apps_to_close = ["notepad.exe", "chrome.exe", "word.exe"]
time.sleep(25)

send_notification("Timer is started", "You will be notified about your working time")

while True:
    # First check for 3 hours, then notify
    if counter_hour == 3:
        # Notify the user about the apps being closed
        send_notification("Closing Apps Soon", "You have reached 3 hours of usage. The apps will be closed shortly.")
        
        # Give a brief time before closing the apps
        time.sleep(30)
        
        # Close apps
        for app in apps_to_close:
            os.system(f"taskkill /F /IM {app}")
        
        # Notify the user after closing apps
        send_notification("Apps are closed", "Your working time has reached 3 hours, so you need to take a compulsory break.")
        
        # Exit the program after closing the apps
        break
    
    time.sleep(3600)  # Waits 1 hour
    
    # Notify about the usage time
    send_notification("Usage of computer for 1 hour", 
                      "You have been using the computer for 1 hour. Consider taking a break.")
    
    # Wait for 5-minute break
    time.sleep(300)  # Wait 5 minutes
    send_notification("Break Over", "The timer has been rescheduled. You can resume your work.")
    
    counter_hour += 1  # Increase the hour count
