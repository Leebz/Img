from PIL import Image
import cv2
import os

PATHNAME = 'datas/'
OUTPUT = '1103res/'
files = []
size_m = 1043
size_n = 549

def get_all_files(path):
    list = os.listdir(path)
    return list

def convert_img(img):
    im = cv2.imread(PATHNAME+img)
    image = Image.fromarray(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
    # image = image.convert('L')
    image = image.resize((size_m, size_n), Image.ANTIALIAS)
    img = rename(img)
    image.save(OUTPUT+img, quality=100, dpi=(300.0, 300.0))

def rename(img):
    list = img.split('.')
    if list[1]!='jpg':
        img = list[0]+'.jpg'
    return img


if __name__ == "__main__":
    files = get_all_files(PATHNAME)

    for i in range(len(files)):
        convert_img(files[i])



