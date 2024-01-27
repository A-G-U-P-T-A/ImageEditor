from concurrent.futures import ThreadPoolExecutor
import os


class ImageConversionService:
    def __init__(self, transformation_service, file_service):
        self.transformation_service = transformation_service
        self.file_service = file_service

    def convert_single_image(self, source, target_dir, target_format):
        target_path = os.path.join(target_dir, os.path.splitext(os.path.basename(source))[0])
        self.transformation_service.convert_image_format(source, target_path, target_format)

    def convert_bulk_images(self, source_dir, target_dir, target_format, max_concurrent=5):
        images = self.file_service.get_images_from_directory(source_dir)
        with ThreadPoolExecutor(max_workers=max_concurrent) as executor:
            for image_path in images:
                executor.submit(self.convert_single_image, image_path, target_dir, target_format)
