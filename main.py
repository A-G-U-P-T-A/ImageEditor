# # This is a sample Python script.
# from engine.FileService import FileService
# from engine.ImageConversionService import ImageConversionService
# from engine.ImageTransformationService import ImageTransformationService
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# # def print_hi(name):
# #     # Use a breakpoint in the code line below to debug your script.
# #     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# #
# #
# # # Press the green button in the gutter to run the script.
# # if __name__ == '__main__':
# #     print_hi('PyCharm')
# #
# # # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
# transformation_service = ImageTransformationService()
# file_service = FileService()
# conversion_service = ImageConversionService(transformation_service, file_service)
#
# # Convert a single image
# # conversion_service.convert_single_image('path/to/source/image.jpg', 'path/to/target/directory', 'png')
#
# # Bulk convert images
# if __name__ == '__main__':
#     conversion_service.convert_bulk_images(r'C:\Users\ASUS\Desktop\icons', r'C:\Users\ASUS\Desktop\icons', 'jpeg')

import sys
from PyQt5.QtWidgets import QApplication, QTreeView, QFileSystemModel, QVBoxLayout, QWidget


class FileExplorer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("File Explorer")
        self.setGeometry(100, 100, 800, 600)

        # Create a file system model
        model = QFileSystemModel()
        model.setRootPath('')  # Setting root to the entire file system
        tree = QTreeView(self)
        tree.setModel(model)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(tree)
        self.setLayout(layout)


def main():
    app = QApplication(sys.argv)
    ex = FileExplorer()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
