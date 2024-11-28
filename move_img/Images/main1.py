import os 

downloads_folder = os.path.expanduser("~/Downloads")

"""
Using `os.access` function to check the permissions
for the `~/Downloads` directory within my script.
"""

if os.access(downloads_folder, os.R_OK):
    print('Read access is allowed.')

if os.access(downloads_folder, os.W_OK):
    print('Write access is allowed.')