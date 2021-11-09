from setpfp import setpfp
from dotenv import load_dotenv
from file_loader import listImages
import os
from random import choice
import time
from timelog import getTime

# * Load Environment Variable
load_dotenv()


IMAGE_DIR = os.getenv("IMAGE_DIR")

if IMAGE_DIR is None:
    raise Exception("IMAGE_DIR is not set")

current_image = None

while True:
    imageLists = listImages(IMAGE_DIR)
    print(f"Successfully listed {len(imageLists)} images")

    selectedImage = choice(imageLists)

    if current_image == selectedImage:
        continue
    current_image = selectedImage

    setpfp(IMAGE_DIR + "/" + selectedImage)
    print(f"[{getTime()}] Image has been set: {selectedImage}")
    time.sleep(300)
