import os
import sys
import argparse
from PIL import Image


def bytes_to_megabytes(bytes: int) -> int:
    return bytes * (1 / 1024**2)


def file_path(filepath: str) -> str:
    if os.path.isfile(filepath):
        return filepath
    else:
        raise FileNotFoundError(filepath)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="read image from filepath and save a compressed version"
    )
    parser.add_argument("filepath", type=file_path, help="full filepath to image")
    parser.add_argument(
        "-q",
        "--quality",
        type=int,
        help="compression quality, [0, 100], default 90 (slight compression).",
        metavar="QUALITY",
        nargs="?",
        choices=list(range(1, 101)),
        default=90,
    )
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="verbose filesize change information",
    )
    group.add_argument(
        "-s", "--suppress", action="store_true", help="suppress print statements"
    )
    args = parser.parse_args()

    image_path = args.filepath
    image_quality = args.quality
    verbose = args.verbose
    suppress = args.suppress

    png_image = Image.open(image_path)
    directory, filename_with_extension = os.path.split(image_path)
    filename, _ = os.path.splitext(filename_with_extension)
    save_path = os.path.join(directory, ((f"COMPRESSED-QUAL={image_quality}_{filename}") + '.jpg'))
    jpg_image = png_image.convert('RGB')
    jpg_image.save(save_path, quality=image_quality, optimize=True)
    original_size = bytes_to_megabytes(os.path.getsize(image_path))
    compressed_size = bytes_to_megabytes(os.path.getsize(save_path))
    compression_size_drop = original_size - compressed_size
    compression_percent_decrease = (compression_size_drop / original_size) * 100

    if not suppress:
        if verbose:
            print("Image compression level:", image_quality)
            print("Original filesize:", str(round(original_size, 2)), "MB")
        print("Compressed filesize:", str(round(compressed_size, 2)), "MB", end="")

        if verbose:
            print(
                f" ({-1 * round(compression_size_drop, 2)} MB, {-1 * round(compression_percent_decrease, 2)}%)"
            )
        else:
            print()


if __name__ == "__main__":
    main()
