from PIL import Image


def imgProcessor(directoryFromTakeImages, directoryWhereSaveImages, filename):
    img = Image.open(f'{directoryFromTakeImages}{filename}')

    basewidth = 4032
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))

    resized_img = img.resize((basewidth, hsize), Image.ANTIALIAS)

    resized_img.save(f'{directoryWhereSaveImages}/{filename}', 'jpeg')
    print('all done!')
