# Help
```
$ python3 compress.py --help
usage: compress.py [-h] [-q QUALITY] [-v | -s] filepath

read image from filepath and save a compressed version

positional arguments:
  filepath              full filepath to image

optional arguments:
  -h, --help            show this help message and exit
  -q QUALITY, --quality QUALITY
                        compression quality, [0, 100], default 90 (slight
                        compression).
  -v, --verbose         verbose filesize change information
  -s, --suppress        suppress print statements
```
# Usage Examples
```
$ python3 compress.py
usage: compress.py [-h] [-q QUALITY] [-v | -s] filepath
compress.py: error: the following arguments are required: filepath
```
```
$ python3 compress.py /home/ryan/Downloads/image.png
Compressed filesize: 0.77 MB
```
```
$ python3 compress.py /home/ryan/Downloads/image.png -v
Image compression level: 90
Original image filetype: .png
Original filesize: 7.3 MB
Compressed jpg filesize: 0.77 MB (-6.53 MB, -89.43%)
```
```
$ python3 compress.py /home/ryan/Downloads/image.png -s
```
```
$ python3 compress.py /home/ryan/Downloads/image.png -v -q 50
Image compression level: 50
Original image filetype: .png
Original filesize: 7.3 MB
Compressed jpg filesize: 0.24 MB (-7.06 MB, -96.7%)
```
