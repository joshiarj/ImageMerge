import os
from send2trash import send2trash as trash
from PIL import Image as img

path = 'files/'
screenshot_folder = path+'screenshots/'

new_width, new_height = (540, 960)  # Dimensions to resize each image to
base_image = img.new(mode='RGB', size=(1620, 960))  # Base image to paste resized images upon, default color='black'
paste_x, paste_y = (0, 0)  # Starting co-ordinates for pasting onto base image

files = sorted(os.listdir(screenshot_folder))  # , reverse=True)  # sorted by name, uncomment if descending
# print(files)

for i in range(0, 3):  # Currently merging 3 files at a time
    im = img.open(screenshot_folder+files[i])
    im_rs = im.resize((new_width, new_height), img.ANTIALIAS)
    base_image.paste(im_rs, (paste_x, paste_y))
    paste_x += 540


def save_file():  # Save to a level above 'screenshots' folder - into 'files'
    base_image.save(path+merged_filename)
    print('Final image saved as: "{}"'.format(merged_filename))
    # base_image.show()
    if input('\nMove screenshot files to Trash? [Y/N]: ').lower() == 'y':
        delete_files()
    exit(0)


def delete_files():  # Send screenshots to Trash/Recycle Bin after merge
    for i in range(0, 3):
        print('File "{}" successfully moved to Trash!'.format(files[i]))
        trash(screenshot_folder+files[i])


# Ask for filename, check if file already exists, and save
while True:
    merged_filename = input('Enter new image filename: ') + '.png'
    if os.listdir(path).__contains__(merged_filename):
        confirm = input('File "{}" already exists! Replace with this one? [Y/N]: '.format(merged_filename))
        if confirm.lower() == 'y':
            save_file()
    else:
        save_file()
