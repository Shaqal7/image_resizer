import sys
import os.path
from PIL import Image

directoryFromTakeImages = sys.argv[1]  # Photos/
directoryWhereSaveImages = sys.argv[2]  # Converted/

# check if directoryWhereSaveImages not exists CREATE it
if not os.path.exists(directoryWhereSaveImages):
    try:
        os.mkdir(directoryWhereSaveImages)
    except OSError:
        print("Creation of the directory failed")
    else:
        print("Successfully created the directory")

for filename in os.listdir(directoryFromTakeImages):
    img = Image.open(f'{directoryFromTakeImages}{filename}')

    basewidth = 4032
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))

    resized_img = img.resize((basewidth, hsize), Image.ANTIALIAS)

    resized_img.save(f'{directoryWhereSaveImages}/{filename}', 'jpeg')
    print('all done!')
