import os
import shutil
import time
import psutil

destination_directory = r'C:\Users\Public\mycreation'

# Get removable drives
def get_usb_drives():
    return [p.device for p in psutil.disk_partitions() if 'removable' in p.opts]

# Copy files from USB to destination
def copy_files(src, dest):
    os.makedirs(dest, exist_ok=True)
    for root, _, files in os.walk(src):
        for file in files:
            try:
                shutil.copy(os.path.join(root, file), os.path.join(dest, file))
                print(f"Copied: {file}")
            except Exception as e:
                print(f"Error copying {file}: {e}")

# Monitor and copy from new USB drives
def monitor_usb():
    processed = set()
    while True:
        for drive in get_usb_drives():
            if drive not in processed:
                print(f"USB detected: {drive}")
                copy_files(drive, destination_directory)
                processed.add(drive)
        time.sleep(5)

if __name__ == '__main__':
    print("Monitoring USB drives...")
    monitor_usb()
