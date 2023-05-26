import os
import shutil

"""
Creating a downloads folder and images folder,
then navigating the folders.
"""
downloads_folder = os.path.expanduser("/Users/thaophamsmacbook/Downloads")
# print(f'downloads_folder: {downloads_folder}')
# images_folder = os.path.expanduser("/Applications/Studying/Github/Python/move_img/Images")
images_folder = os.path.expanduser("/Applications/Studying/Github/Python/move_img/Images")
# print(f'images_folder: {images_folder}')
"""
Checking if the image folder exist
"""
if not os.path.exists(images_folder):
    os.makedirs(images_folder) # Creating the folder if not exist
    # print(f'images_folder: {images_folder}')
"""
Looping through the file's names in the download folde.
If the file ends with '.png' or '.jpg' or '.jpeg',
then move it into the img_folder
"""
for file_name in os.listdir(downloads_folder):
    if file_name.endswith('.png') or file_name.endswith('.jpg') or file_name.endswith('.jpeg'):
        file_path = os.path.join(downloads_folder, file_name) # Getting the file's path by joining
        shutil.move(file_path,images_folder)