from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging
import time
import sys
import os
import shutil

# Append all files in the downloads directory to a list
USERNAME = os.getlogin()


# Make sorting functions with exceptions
class FileMoved(Exception):
    pass


def sort_by_extension(file: str, target_dir: str, *extensions: tuple):
    if file.endswith(extensions):
        while file.split('\\')[4] not in os.listdir(target_dir):
            print("moving...")
            try:
                shutil.move(file, target_dir)
            except FileNotFoundError:
                continue
        print("Moved!")
        raise FileMoved


def sort_by_name(file: str, target_dir: str, words: str):
    if words in file:
        while file.split('\\')[4] not in os.listdir(target_dir):
            print("moving...")
            try:
                shutil.move(file, target_dir)
            except FileNotFoundError:
                continue

        print("moved!")
        raise FileMoved

# sort the file after the file is downloaded in the downloads folder


class MonitorFolder(FileSystemEventHandler):

    def on_created(self, event):
        print(file := event.src_path, event.event_type)
        print(file)
        print(repr(file))
        file_name = file.split('\\')[4]
        downloads_dir = os.listdir(r'C:\Users\{0}\Downloads'.format(USERNAME))
        try:
            sort_by_extension(file, r'C:\Users\{0}\Pictures\Temp Images'.format(
                USERNAME), '.jpg', '.jpeg', '.png', '.gif')
            sort_by_extension(file, r'C:\Users\{0}\Desktop\Books and Comics'.format(
                USERNAME), 'epub', 'mobi', 'cbz', 'cbr')
            sort_by_extension(file, r'C:\Users\suhay\AppData\Roaming\.minecraft\resourcepacks'.format(
                USERNAME), 'epub', 'mobi', 'cbz', 'cbr')
            sort_by_name(
                file, r'C:\Users\suhay\AppData\Roaming\.minecraft\resourcepacks'.format(USERNAME), '§')
        except FileMoved:
            print("file moved")

# use watchdog to check when a file is downloaded in the downloads folder


path = r'C:\Users\suhay\Downloads'

event_handler = MonitorFolder()
observer = Observer()
observer.schedule(
    event_handler, path=path)
observer.start()

while True:
    time.sleep(1)
