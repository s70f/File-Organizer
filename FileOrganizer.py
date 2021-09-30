from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging
import time
import sys
import os
import shutil

# Append all files in the downloads directory to a list
USERNAME = os.getlogin()

files = [file for file in os.listdir(
    r'C:\Users\{0}\Desktop\To-Do'.format(USERNAME))]
print(files)

# sorting by extension function


def sort_by_extension(file: str, target_dir: str, *extensions: tuple):
    if file.endswith(extensions):
        shutil.move(r'C:\Users\{0}\Desktop\To-Do\{1}'.format(USERNAME,
                    file), target_dir)


def sort_by_name(file: str, target_dir: str, words: str):
    if words in file:
        shutil.move(r'C:\Users\{0}\Desktop\To-Do\{1}'.format(USERNAME,
                    file), target_dir)


# sorting
for file in files:
    sort_by_extension(file, r'C:\Users\{0}\Pictures\Temp Images'.format(
        USERNAME), '.jpg', '.jpeg', '.png', '.gif')
    sort_by_extension(file, r'C:\Users\{0}\Desktop\Books and Comics'.format(
        USERNAME), 'epub', 'mobi', 'cbz', 'cbr')
    sort_by_name(
        file, r'C:\Users\{0}\Pictures\Temp Images'.format(USERNAME), '§')


# use watchdog to check when a file is downloaded in the downloads folder


class MonitorFolder(FileSystemEventHandler):

    def on_created(self, event):
        print(event.src_path, event.event_type)


path = r'C:\Users\suhay\Downloads'

event_handler = MonitorFolder()
observer = Observer()
observer.schedule(
    event_handler, path=path)
observer.start()

while True:
    time.sleep(1)
