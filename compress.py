from abc import ABCMeta
import os
import sys
import argparse
from PIL import Image

DEFAULT_QUALITY = 90
assert (
    DEFAULT_QUALITY >= 0 and DEFAULT_QUALITY <= 100
)  #  PIL save image quality range is [0, 100]
assert (
    DEFAULT_QUALITY % 5 == 0
)  # make adaptive compression easier, rather than search all 100 possibilities
SAVED_IMAGES = (
    []
)  #  should only have one saved image and deleted failed attempts with adpative compression


def bytes_to_megabytes(bytes: int) -> int:
    """Convert bytes to mebibytes."""
    return bytes * (1 / 1024 ** 2)


def file_path(filepath: str) -> str:
    """Special type for argparse, a filepath."""
    if os.path.isfile(filepath):
        return filepath
    else:
        raise FileNotFoundError(filepath)


def positive_number(num: str) -> int:
    """Special type for argparse, a positive number."""
    num = int(num)
    if num < 0:
        raise argparse.ArgumentTypeError(
            f"Adaptive compression filesize in MiB must be positive, given {str(num)}."
        )
    return num


def main() -> None:
    parser = argparse.ArgumentParser(
        description="read image from filepath and save a compressed version"
    )
    parser.add_argument("filepath", type=file_path, help="full filepath to image")
    group_quality = parser.add_mutually_exclusive_group(required=False)
    group_quality.add_argument(
        "-q",
        "--quality",
        type=int,
        help="compression quality, [0, 100], default 90 (slight compression).",
        metavar="QUALITY",
        choices=list(range(1, 101)),
        default=DEFAULT_QUALITY,
    )
    group_quality.add_argument(
        "-a",
        "--adaptive",
        type=positive_number,
        help="filesize in MiB that the scipt will attempt to compress to less than",
    )
    group_verbosity = parser.add_mutually_exclusive_group(required=False)
    group_verbosity.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="verbose filesize change information",
    )
    group_verbosity.add_argument(
        "-s", "--suppress", action="store_true", help="suppress print statements"
    )
    args = parser.parse_args()

    image_path = args.filepath
    current_image_quality = args.quality
    verbose = args.verbose
    suppress = args.suppress
    adaptive = args.adaptive

    directory, filename_with_extension = os.path.split(image_path)
    filename, extension = os.path.splitext(filename_with_extension)
    original_size = bytes_to_megabytes(os.path.getsize(image_path))

    def save_image(image_quality=DEFAULT_QUALITY) -> tuple[str, int]:
        if verbose:
            print("Attempting quality setting:", current_image_quality)
        image = Image.open(image_path)
        save_path = os.path.join(
            directory, ((f"COMPRESSED-QUAL={image_quality}_{filename}") + ".jpg")
        )
        jpg_image = image.convert("RGB")
        jpg_image.save(save_path, quality=image_quality, optimize=True)
        compressed_size = bytes_to_megabytes(os.path.getsize(save_path))
        return save_path, compressed_size

    if current_image_quality == DEFAULT_QUALITY:
        save_path, compressed_size = save_image()
    else:
        save_path, compressed_size = save_image(image_quality=current_image_quality)

    def delete_images():
        assert len(SAVED_IMAGES) != 0
        if len(SAVED_IMAGES) > 1:
            for filepath in SAVED_IMAGES[0:-1]:
                os.remove(filepath)

    SAVED_IMAGES.append(save_path)
    if adaptive is not None:
        if compressed_size > adaptive:
            for current_image_quality in (
                possible_quality_values := list(range(DEFAULT_QUALITY - 5, -1, -5))
            ):  #  already tried for first quality setting
                save_path, compressed_size = save_image(
                    image_quality=current_image_quality
                )
                SAVED_IMAGES.append(save_path)
                if compressed_size < adaptive:
                    break
            else:
                delete_images()
                Exception(
                    f"Adaptive compression was not able to compress "
                    + "original image filesize from {original_size} MiB to "
                    + "{adaptive} MiB, only acheived compression to"
                    + " {compressed_size} MiB"
                )

    compression_size_drop = original_size - compressed_size
    compression_percent_decrease = (compression_size_drop / original_size) * 100

    delete_images()

    if not suppress:
        if verbose:
            print("Image compression level:", current_image_quality)
            print("Original image filetype:", extension)
            print("Original filesize:", str(round(original_size, 2)), "MB")
        print(
            f"Compressed{' jpg ' if verbose else ' '}filesize:",
            str(round(compressed_size, 2)),
            "MB",
            end="",
        )  #  this line is continued in next print statement

        if verbose:
            print(
                f" ({-1 * round(compression_size_drop, 2)} MB, {-1 * round(compression_percent_decrease, 2)}%)"
            )
        else:
            print()


if __name__ == "__main__":
    main()
