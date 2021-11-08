from setpfp import setpfp
from dotenv import load_dotenv
from file_loader import listImages
import os
from random import choice
import time

# * Load Environment Variable
load_dotenv()


IMAGE_DIR = os.getenv("IMAGE_DIR")

if IMAGE_DIR is None:
    raise Exception("IMAGE_DIR is not set")

current_image = None

while True:
    imageLists = listImages(IMAGE_DIR)
    selectedImage = choice(imageLists)

    if current_image == selectedImage:
        continue

    current_image = selectedImage

    setpfp(IMAGE_DIR + "/" + choice(imageLists))
    print(f"Image has been set: {current_image}")
    time.sleep(300)
