import numpy as np
import os
from PIL import Image

path = "images/"
dirs = os.listdir(path)

print(dirs)


def resize_images():
    for item in dirs:
        if os.path.isfile(path + item):
            im = Image.open(path + item)
            f, e = os.path.splitext(path + item)
            imResize = im.resize((512, 512), Image.ANTIALIAS)
            imResize.save('resized_images/' + str(f.split('/')[1]) + ' resized.png', 'PNG', quality=90)


resize_images()

images_array = []

for item in dirs:
    if os.path.isfile(path + item):
        im = Image.open(path + item)
        images_array.append(np.array(im))

print(len(images_array))
