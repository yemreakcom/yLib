from exif import Image
import os.path as osp
import glob

IMAGE_PATH = r"C:\Users\Yedhrab\Downloads\in_wild\label_in_wild\images"


def metadata():
    images = [image for image in glob.glob(osp.join(IMAGE_PATH, '*.jpg'))]
    exif_images = []

    for image in images:
        with open(image, "rb") as image_file:
            print(image)
            exif_images.append(Image(image_file))

    return exif_images


images = metadata()
for image in images:
    print(image.has_exif)
