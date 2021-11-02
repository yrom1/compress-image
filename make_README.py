import os
import re
import subprocess
from textwrap import dedent
from typing import List

import requests

JPG_URL = "https://upload.wikimedia.org/wikipedia/commons/b/bd/Malanggan_Maske_Neuirland_im_%C3%9Cberseemuseum_a_05.JPG"
TEST_JPG_FILEPATH = "image.jpg"


def download_image_from_url(url: str, filename=None) -> None:
    """Downloads image from url in current directory with the URL's image filename if not specified."""
    original_filename, extension = os.path.splitext(url.split("/")[-1])
    if filename is None:
        filename = original_filename
    # As of February 15, 2010, Wikimedia sites require a HTTP User-Agent header
    # for all requests.
    user_agent = {"User-agent": "Mozilla/5.0"}
    r = requests.get(url, allow_redirects=False, headers=user_agent)
    open(filename + extension.lower(), "wb").write(r.content)


FILENAME, _ = os.path.splitext(TEST_JPG_FILEPATH)
download_image_from_url(JPG_URL, FILENAME)

with open("README.md", "w") as f:

    def write_subprocess_to_markdown(command_list: List[str]) -> None:
        f.write("```\n")
        f.write("$ " + " ".join(command_list))
        f.write("\n")
        result = subprocess.run(command_list, capture_output=True, text=True)
        f.write(result.stdout)
        f.write(result.stderr)
        f.write("```\n")

    badges = """
    <p align="left">
    <a href="https://github.com/yrom1/compress-image/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
    <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
    </p>
    """
    f.write(dedent(badges))
    f.write("\n")
    f.write("# Help\n")
    write_subprocess_to_markdown(["python3", "compress.py", "--help"])
    f.write("# Usage Examples\n")
    write_subprocess_to_markdown(["python3", "compress.py"])
    write_subprocess_to_markdown(["python3", "compress.py", TEST_JPG_FILEPATH])
    write_subprocess_to_markdown(["python3", "compress.py", TEST_JPG_FILEPATH, "-v"])
    write_subprocess_to_markdown(["python3", "compress.py", TEST_JPG_FILEPATH, "-s"])
    write_subprocess_to_markdown(
        ["python3", "compress.py", TEST_JPG_FILEPATH, "-v", "-q", "50"]
    )
    write_subprocess_to_markdown(
        ["python3", "compress.py", TEST_JPG_FILEPATH, "-a", "1", "-v"]
    )

JPG_FILES = [
    file for file in os.listdir(".") if os.path.isfile(file) and file[-4::] == ".jpg"
]
for jpg in JPG_FILES:
    os.remove(jpg)
