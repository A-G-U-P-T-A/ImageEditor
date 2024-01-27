# from skimage import io, color
# import os
#
#
# class ImageTransformationService:
#     @staticmethod
#     def convert_image_format(source_path, target_path, target_format):
#         image = io.imread(source_path)
#         io.imsave(f"{target_path}.{target_format}", image)
from PIL import Image
import os


class ImageTransformationService:
    @staticmethod
    def convert_image_format(source_path, target_path, target_format):
        with Image.open(source_path) as img:
            target_file = f"{target_path}.{target_format}"
            img.save(target_file, format=target_format.upper())
