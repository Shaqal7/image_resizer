import sys
import os.path
from imgProcessor import imgProcessor


directoryFromTakeImages = sys.argv[1]  # Photos/
directoryWhereSaveImages = sys.argv[2]  # Converted/

# for test
# directoryFromTakeImages = 'Photos/'  # Photos/
# directoryWhereSaveImages = 'Converted/'  # Converted/

if not os.path.exists(directoryWhereSaveImages):
    try:
        os.mkdir(directoryWhereSaveImages)
    except OSError:
        print("Creation of the directory failed")
    else:
        print("Successfully created the directory")

for filename in os.listdir(directoryFromTakeImages):
    imgProcessor(directoryFromTakeImages, directoryWhereSaveImages, filename)
