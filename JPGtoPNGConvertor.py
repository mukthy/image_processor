import os.path
import sys
from PIL import Image

source = sys.argv[1]
dest = sys.argv[2]

isdir = os.path.isdir(dest)
files = os.listdir(source)


def convertor(dest):
    print("Directory is not available, so creating a new one!")
    for file in files:
        print(file)
        image = Image.open(f'./{source}/{file}')
        name = os.path.basename(f'./{source}/{file}')
        text = os.path.splitext(name)[0]
        image.save(f'./{dest}/{text}.png', 'png')


if isdir is False:
    os.mkdir(dest)
    convertor(dest)

else:
    print("Directory is available")
    convertor(dest)
# print(files)
# print(isdir)
