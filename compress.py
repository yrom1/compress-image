import os
import sys
import argparse
from PIL import Image

def bytes_to_megabytes(bytes: int) -> int:
    return bytes * (1 / 10**6)

def file_path(string):
    if os.path.isfile(string):
        return string
    else:
        raise FileNotFoundError(string)

def main() -> None:
    parser=argparse.ArgumentParser(description='Read image from filepath and save a compressed version.')
    parser.add_argument('-f', '--filepath', type=file_path, help='Full filepath to image.')
    parser.add_argument('-q', '--quality', type=int, help='Compression quality, range [0, 100], default 90 (slight compression).', metavar='quality', nargs='?', choices=list(range(1,101)), default=90)
    parser.add_argument('-v','--verbose', action='store_true', help='Full filepath to image.')
    args = parser.parse_args()
    
    image_path = args.filepath
    image_quality = args.quality
    verbose = args.verbose

    image = Image.open(image_path)
    directory, filename = os.path.split(image_path)
    save_path = os.path.join(directory, (f'COMPRESSED-QUAL={image_quality}_{filename}'))
    image.save(save_path, quality=args.quality)
    
    original_size = bytes_to_megabytes(os.path.getsize(image_path))
    compressed_size = bytes_to_megabytes(os.path.getsize(save_path))
    compression_size_drop = original_size - compressed_size
    compression_percent_decrease = (compression_size_drop / original_size) * 100
 
    if verbose:
        print('Image compression level:', image_quality)
        print('Original filesize:', str(round(original_size, 2)), 'MB')
    print('Compressed filesize:', str(round(compressed_size, 2)), 'MB', end='')
    
    if verbose:
        print(f' (-{round(compression_size_drop, 2)} MB, -{round(compression_percent_decrease, 2)}%)')
    else:
        print()

if __name__ == '__main__':
    main()
