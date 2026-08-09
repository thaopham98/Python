from PIL import Image, ImageOps

# python .\python_img.py

image_path = r"C:\Users\Thao\Pictures\damianwayne_by_danmora_2025.jpg"

# print(f"Image Size: {img.size}")

# # img.show() # open the image

# t_img = ImageOps.exif_transpose(img)

# print(f"Transposed Image: {t_img}")

# t_img.show()

## Convert RBG to CIELAB

# import cv2
import numpy as np
try:
    # print(f"Image Bytes: {im_bytes}") 
    img = Image.open(image_path)
    im_bytes = img.tobytes()

    width, height = img.size

    ## Create 3D array (height, width, 3) of type int8
    rgb_array = np.frombuffer(im_bytes, dtype=np.uint8).reshape(((height, width, 3))) # the (3) represents the three RGB color channels

    ## transpose width and height
    rgb_array = rgb_array.transpose(1, 0, 2).copy()

    
except IOError:
    print("Error")
