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
                        compression quality, [0, 100], default 90
                        (slight compression).
  -v, --verbose         verbose filesize change information
  -s, --suppress        suppress print statements
```

# Usage Examples
```
$ python3 compress.py '/home/ryan/Downloads/Eunji_Digital Photobook vol.2_019.jpg'
Compressed filesize: 1.86 MB
```
```
$ python3 compress.py '/home/ryan/Downloads/Eunji_Digital Photobook vol.2_019.jpg' -v
Image compression level: 90
Original image filetype: .jpg
Original filesize: 8.07 MB
Compressed jpg filesize: 1.86 MB (-6.21 MB, -76.96%)
```
```
$ python3 compress.py '/home/ryan/Downloads/Eunji_Digital Photobook vol.2_019.jpg' -s
$ 
```
```
$ python3 compress.py '/home/ryan/Downloads/Eunji_Digital Photobook vol.2_019.jpg' -v -q 50
Image compression level: 50
Original image filetype: .jpg
Original filesize: 8.07 MB
Compressed jpg filesize: 0.45 MB (-7.62 MB, -94.45%)
```
