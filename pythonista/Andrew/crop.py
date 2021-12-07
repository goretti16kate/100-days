from CSE8AImage import *
from PIL import Image

img = load_img('catty.jpeg')
region_width = 200
region_height = 200
def check_validity(img, region_width, region_height):
    #to ensure that all conditions are met
    #should be greater than zero,
    #region_width should be less than or equal to the width
    # 3.region_height should be less than or equal to the width
    if region_width and region_height > 0 and  region_width <= width(img) and region_height <= height(img):
        return True
    else:
        return False

    

def crop(img, region_width, region_height):
    #open image
    img = Image.open('catty.jpeg')
    # pixel sizes of where to crop
    values = (0,0, region_width, region_height)
    #crop image
    cropped_image = img.crop(values)
    #save image
    cropped_image.save('filename.jpg')


    #save_img(created, 'filename')
    img_str_to_file(img, 'fileee')
    




check_validity(img, region_width, region_height)
crop(img, region_width, region_height )