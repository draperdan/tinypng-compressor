import os
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from base64 import b64encode
import sys
import getopt
import argparse

import settings

key = settings.API_KEY
accepted_extensions = settings.ACCEPTED_EXTENSIONS


def compress(argv):
    """
    Compress a directory of png/jpg images using the TinyPNG/TinyJPG service.
    """
    parser = argparse.ArgumentParser(description='Compress files in directory')
    parser.add_argument(
        dest='filenames',
        metavar='filename',
        nargs='*',
    )
    parser.add_argument(
        '-i',
        '--i',
        dest='inpath',
        action='store',
        required=True,
        help='directory containing files to compress',
    )
    parser.add_argument(
        '-o',
        '--o',
        dest='outpath',
        action='store',
        help='optional path for output directory',
    )
    args = parser.parse_args()



    # try:
    #     if dirpath:
    #         file_list = os.listdir(dirpath)
    #         for file in file_list:
    #             ext = os.path.splitext(file)[-1].lower()
    #             if ext in accepted_extensions:
    #                 request = Request(
    #                     "https://api.tinypng.com/shrink",
    #                     open(os.path.join(dirpath, file), "rb").read()
    #                 )
    #                 cafile = None
    #                 # Uncomment below if you have trouble validating our SSL certificate.
    #                 # Download cacert.pem from: http://curl.haxx.se/ca/cacert.pem
    #                 # cafile = dirname(__file__) + "/cacert.pem"
    #                 auth = b64encode(bytes("api:" + key, "ascii")).decode("ascii")
    #                 request.add_header("Authorization", "Basic {}".format(auth))
    #                 try:
    #                     response = urlopen(request, cafile=cafile)
    #                     result = urlopen(
    #                         response.getheader("Location"), cafile=cafile).read()
    #                     output = os.path.join(
    #                         dirpath,
    #                         os.path.splitext(file)[0] + '_tny' + os.path.splitext(file)[1]
    #                     )
    #                     open(output, "wb").write(result)
    #                 except HTTPError as error:
    #                     print('Error: {}'.format(error.reason))
    #     else:
    #         print('No directory path specified.')
    # except FileNotFoundError:
    #     print('The directory specified doesn\'t exist.')

if __name__ == "__main__":
    
    # compress(sys.argv[1:])
