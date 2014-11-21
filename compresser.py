import os
from urllib.request import Request, urlopen
from base64 import b64encode
from sys import argv

import settings

key = settings.API_KEY
accepted_extensions = settings.ACCEPTED_EXTENSIONS


def compress(path):
    file_list = os.listdir(path)
    for file in file_list:
        ext = os.path.splitext(file)[-1].lower()
        if ext in accepted_extensions:
            request = Request(
                "https://api.tinypng.com/shrink",
                open(os.path.join(path, file), "rb").read()
            )
            cafile = None
            # Uncomment below if you have trouble validating our SSL certificate.
            # Download cacert.pem from: http://curl.haxx.se/ca/cacert.pem
            # cafile = dirname(__file__) + "/cacert.pem"
            auth = b64encode(bytes("api:" + key, "ascii")).decode("ascii")
            request.add_header("Authorization", "Basic %s" % auth)

            response = urlopen(request, cafile=cafile)
            if response.status == 201:
                # Compression was successful, retrieve output from Location header.
                result = urlopen(
                    response.getheader("Location"), cafile=cafile).read()
                output = os.path.join(
                    path,
                    os.path.splitext(file)[0] + '_compressed' + os.path.splitext(file)[1]
                )
                open(output, "wb").write(result)
            else:
                # Something went wrong! You can parse the JSON body for details.
                print("Compression failed")

if __name__ == "__main__":
    try:
        path_input = argv[1]
        compress(path_input)
    except IndexError:
        print("You didn't enter a path.")
