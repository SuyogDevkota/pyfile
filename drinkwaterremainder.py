import time
from plyer import notification
title = "Drink water reminder"
message = "This is the time. Drink water now"
def remainder():
    notification.notify(
        title=title,
        message=message,
        timeout=30  # The notification stays for 30 seconds
    )

while True:
    remainder()
    time.sleep(3600)
