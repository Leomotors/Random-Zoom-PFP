from setpfp import setpfp
from dotenv import load_dotenv
from file_loader import listImages
import os
from random import choice

# * Load Environment Variable
load_dotenv()


IMAGE_DIR = os.getenv("IMAGE_DIR")

if IMAGE_DIR is None:
    raise Exception("IMAGE_DIR is not set")

imageLists = listImages(IMAGE_DIR)

setpfp(IMAGE_DIR + "/" + choice(imageLists))

print("Image has been set!")
