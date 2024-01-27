from pathlib import Path
from enum import Enum, auto


class ImageFormat(Enum):
    JPG = auto()
    JPEG = auto()
    PNG = auto()
    WEBP = auto()
    TIFF = auto()
    BMP = auto()
    ICNS = auto()
    GIF = auto()
    EPS = auto()
    PSD = auto()
    PS = auto()

    @staticmethod
    def get_extensions():
        return {
            '.jpg': ImageFormat.JPG,
            '.jpeg': ImageFormat.JPEG,
            '.png': ImageFormat.PNG,
            '.webp': ImageFormat.WEBP,
            '.tiff': ImageFormat.TIFF,
            '.bmp': ImageFormat.BMP,
            '.icns': ImageFormat.ICNS,
            '.gif': ImageFormat.GIF,
            '.eps': ImageFormat.EPS,
            '.psd': ImageFormat.PSD,
            '.ps': ImageFormat.PS
        }


class FileService:
    @staticmethod
    def get_images_from_directory(directory_path, extensions=None):
        if extensions is None:
            extensions = ImageFormat.get_extensions().keys()
        path = Path(directory_path)
        return [file for file in path.iterdir() if file.suffix.lower() in extensions]
