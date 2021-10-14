import os
import sys
from PIL import Image

def bytes_to_megabytes(bytes: int) -> int:
    return bytes * (1 / 10**6)

def main() -> None:
    """
    Read image path from argv and save it compressed using PIL.
    Arg 1: Full filepath to image.
    Arg 2: Compression quality for PIL, between 0 - 100, default 95.
    """
    image_path = sys.argv[1]
    if not os.path.isfile(image_path):
        raise Exception(f'File {image_path} does not exist.')

    try:
        image_quality = int(sys.argv[2])
        if image_quality < 0 or image_quality > 100:
            raise Exception(f'Requeted image quality {image_quality} out of bounds [0, 100].')
    except IndexError:
        image_quality = 95

    image = Image.open(image_path)
    directory, filename = os.path.split(image_path)
    save_path = os.path.join(directory, (f'COMPRESSED-QUAL={image_quality}' + '_' + filename))
    image.save(save_path, quality = image_quality)
    print('Compressed filesize:', str(round(bytes_to_megabytes(os.path.getsize(save_path)), 2)) + 'MB')


if __name__ == '__main__':
    main()
