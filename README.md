tinypng-compressor
==================

This is a command-line tool to compress a directory of png/jpg files using [TinyPNG](http://tinypng.com)'s compression API.

I love TinyPNG's web-based image compression service, but it found it tedious to upload and download files for compression. I wrote this program to use their API to compress a directory of images, ideally for deployment purposes.

Though this program is written with TinyPNG in mind, I imagine it could easily be swapped for another service such as [Kraken.io](https://kraken.io/).

## Usage

Sign up for a free API key from [TinyPNG](https://tinypng.com/developers)

Set the API key in `settings.py` or via an environment variable (preferred).

Usage: compressor.py [-h] -i INPATH [-o OUTPATH] [filename [filename ...]]

Required arguments:

* `filename`: list of files to compress within a specified directory
* `-i INPATH, --i INPATH`: path to directory containing files to compress

Optional arguments:

* `-h, --help`: show this help message and exit
* `-o OUTPATH, --o OUTPATH`: optional path for output directory

Example: `python compress.py largefile.png -i /Users/patrickbeeson/desktop/test` or `python compress.py largefile.png -i /Users/patrickbeeson/desktop/test -o /Users/patrickbeeson/desktop/compressed`

If no outpath argument is used, your compressed images are created in the same directory with "compressed" appended to the file name.

The service works with either png or jpg files.

## Tests

Note: Tests require the Pillow module: `pip install Pillow`

Run: `python test_compressor.py`

## Contact

Feel free to open a pull request or contact me at patrick@patrickbeeson.com with questions.
