# This is a sample Python script.
from engine.FileService import FileService
from engine.ImageConversionService import ImageConversionService
from engine.ImageTransformationService import ImageTransformationService

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

transformation_service = ImageTransformationService()
file_service = FileService()
conversion_service = ImageConversionService(transformation_service, file_service)

# Convert a single image
# conversion_service.convert_single_image('path/to/source/image.jpg', 'path/to/target/directory', 'png')

# Bulk convert images
if __name__ == '__main__':
    conversion_service.convert_bulk_images(r'C:\Users\ASUS\Desktop\icons', r'C:\Users\ASUS\Desktop\icons', 'jpeg')

