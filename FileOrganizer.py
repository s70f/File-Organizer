import os

# Append all files in the downloads directory to a list
USERNAME = os.getlogin()

files = [file for file in os.listdir(
    r'C:\Users\{0}\Desktop\To-Do'.format(USERNAME))]
print(files)
