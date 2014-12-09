import os
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from base64 import b64encode
import argparse

import settings

key = settings.API_KEY
accepted_extensions = settings.ACCEPTED_EXTENSIONS


def compress(args):
    """
    Compress a directory of png/jpg images using the TinyPNG/TinyJPG service.
    """
    try:
        for file in args.filenames:
            ext = os.path.splitext(file)[-1].lower()
            if ext in accepted_extensions:
                request = Request(
                    "https://api.tinypng.com/shrink",
                    open(os.path.join(args.inpath, file), "rb").read()
                )
                cafile = None
                # Uncomment below if you have trouble validating the SSL cert.
                # Download cacert.pem from: http://curl.haxx.se/ca/cacert.pem
                # cafile = dirname(__file__) + "/cacert.pem"
                auth = b64encode(bytes("api:" + key, "ascii")).decode("ascii")
                request.add_header("Authorization", "Basic {}".format(auth))
                try:
                    response = urlopen(request, cafile=cafile)
                    result = urlopen(
                        response.getheader("Location"), cafile=cafile).read()
                    if args.outpath:
                        output = os.path.join(args.outpath, file)
                    else:
                        output = os.path.join(
                            args.inpath,
                            os.path.splitext(file)[0] + '_tny' + os.path.splitext(file)[1]
                        )
                    open(output, "wb").write(result)
                except HTTPError as error:
                    print('Error: {}'.format(error.reason))
    except FileNotFoundError:
        print('The directory specified doesn\'t exist.')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compress files in directory')
    parser.add_argument(
        dest='filenames',
        metavar='filename',
        nargs='*',
        help='list of files to compress within a specified directory',
    )
    parser.add_argument(
        '-i',
        '--i',
        dest='inpath',
        action='store',
        required=True,
        help='path to directory containing files to compress',
    )
    parser.add_argument(
        '-o',
        '--o',
        dest='outpath',
        action='store',
        help='optional path for output directory',
    )
    args = parser.parse_args()
    compress(args)
