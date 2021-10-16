# Help
```python3 compress.py --help
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
```python3 compress.py
usage: compress.py [-h] [-q QUALITY] [-v | -s] filepath
compress.py: error: the following arguments are required: filepath
```
