from PIL import Image as img
import os

path = 'files/'
file_list = os.listdir(path)
# total_files = sum(1 for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f[0] != '.')  # Counting total files in the folder
new_width, new_height = (540, 960)  # Dimensions to resize each image to
base_image = img.new(mode='RGB', size=(1620, 960), color='white')  # Base image to paste resized images upon
paste_x, paste_y = (0, 0)  # Starting co-ordinates for pasting

for i in range(1, 4):  # Merging 3 screenshots at a time
    im = img.open(path + 'tomerge{}.png'.format(i))
    width, height = im.size
    # print('testpic{}.png dimensions = {}×{}'.format(i, width, height))
    im_rs = im.resize((new_width, new_height), img.ANTIALIAS)
    # print('testpic{}_rs.png dimensions = {}×{}'.format(i, im_rs.size[0], im_rs.size[1]))
    base_image.paste(im_rs, (paste_x, paste_y))
    paste_x += 540


def save_file():
    base_image.save(path + merged_filename)
    print('Final image saved as: "{}"'.format(merged_filename))
    exit(0)


# base_image.show()

# Ask for filename and check if file already exists
while True:
    merged_filename = input('Enter filename: ') + '.png'
    if file_list.__contains__(merged_filename):
        confirm = input('File already exists! Replace with this one? [Y/N]: ')
        if confirm.lower() == 'y':
            save_file()
    else:
        save_file()
