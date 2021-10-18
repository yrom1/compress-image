# Help
```
$ python3 compress.py --help

TEST

TEST
TEST
TEST
usage: compress.py [-h] [-q QUALITY | -a ADAPTIVE] [-v | -s] filepath

read image from filepath and save a compressed version

positional arguments:
  filepath              full filepath to image

optional arguments:
  -h, --help            show this help message and exit
  -q QUALITY, --quality QUALITY
                        compression quality, [0, 100], default 90 (slight
                        compression).
  -a ADAPTIVE, --adaptive ADAPTIVE
                        filesize in MiB that the scipt will attempt to
                        compress to less than
  -v, --verbose         verbose filesize change information
  -s, --suppress        suppress print statements
```
# Usage Examples
```
$ python3 compress.py

TEST

TEST
TEST
TEST
usage: compress.py [-h] [-q QUALITY | -a ADAPTIVE] [-v | -s] filepath
compress.py: error: the following arguments are required: filepath
```
```
$ python3 compress.py image.jpg

TEST

TEST
TEST
TEST
Compressed filesize: 2.3 MB
```
```
$ python3 compress.py image.jpg -v

TEST

TEST
TEST
TEST
Attempting quality setting: 90
Image compression level: 90
Original image filetype: .jpg
Original filesize: 5.95 MB
Compressed jpg filesize: 2.3 MB (-3.64 MB, -61.24%)
```
```
$ python3 compress.py image.jpg -s

TEST

TEST
TEST
TEST
```
```
$ python3 compress.py image.jpg -v -q 50

TEST

TEST
TEST
TEST
Attempting quality setting: 50
Image compression level: 50
Original image filetype: .jpg
Original filesize: 5.95 MB
Compressed jpg filesize: 0.45 MB (-5.5 MB, -92.44%)
```
```
$ python3 compress.py image.jpg -a 1 -v

TEST

TEST
TEST
TEST
Attempting quality setting: 90
Attempting quality setting: 85
Attempting quality setting: 80
Attempting quality setting: 75
Image compression level: 75
Original image filetype: .jpg
Original filesize: 5.95 MB
Compressed jpg filesize: 0.99 MB (-4.96 MB, -83.33%)
```
