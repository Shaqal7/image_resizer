from PIL import Image
import os

def imgProcessor(directory_from, directory_to, filename):
    try:
        img_path = os.path.join(directory_from, filename)
        img = Image.open(img_path)

        basewidth = 4032
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))

        resized_img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        save_path = os.path.join(directory_to, filename)
        
        resized_img.save(save_path, 'jpeg')
        print(f"{filename} processed and saved to {directory_to}")
    except Exception as e:
        print(f"Error processing {filename}. Error: {e}")