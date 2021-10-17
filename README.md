# Help
```
$ python3 compress.py --help
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
                        Filesize in MiB that adaptive compression will attempt
                        to output less than.
  -v, --verbose         verbose filesize change information
  -s, --suppress        suppress print statements
```
# Usage Examples
```
$ python3 compress.py
usage: compress.py [-h] [-q QUALITY | -a ADAPTIVE] [-v | -s] filepath
compress.py: error: the following arguments are required: filepath
```
```
$ python3 compress.py /home/ryan/Downloads/image.png
Compressed filesize: 0.77 MB
```
```
$ python3 compress.py /home/ryan/Downloads/image.png -v
Attempting quality setting: 90
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
Attempting quality setting: 50
Image compression level: 50
Original image filetype: .png
Original filesize: 7.3 MB
Compressed jpg filesize: 0.24 MB (-7.06 MB, -96.7%)
```
```
$ python3 compress.py /home/ryan/Downloads/image.jpg -a 1 -v
Attempting quality setting: 90
Attempting quality setting: 85
Attempting quality setting: 80
Attempting quality setting: 75
Image compression level: 75
Original image filetype: .jpg
Original filesize: 8.81 MB
Compressed jpg filesize: 1.0 MB (-7.81 MB, -88.66%)
```
