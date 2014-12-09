import unittest
import tempfile
import shutil
import os
from PIL import Image
from compressor import compress, create_parser


class TestCompressor(unittest.TestCase):

    def setUp(self):
        self.origdir = os.getcwd()
        self.testdir = tempfile.mkdtemp('tempdir')
        os.chdir(self.testdir)
        self.outputdir = os.path.join(os.getcwd(), 'output')
        self.image = Image.new('RGB', (100, 100), 'white')
        self.image.save('test.png')
        self.image.close()
        self.parser = create_parser()

    def test_with_empty_args(self):
        "Test function exits with no args passed."
        with self.assertRaises(SystemExit):
            self.parser.parse_args([])

    def test_with_bad_filename(self):
        "Test function errors out with non-existant filename."
        with self.assertRaises(FileNotFoundError):
            args = self.parser.parse_args(['test_bad.png', '-i', self.testdir])
            compress(args)

    def test_compresses_images_specified(self):
        "Test function compresses images with filename and input dir args."
        args = self.parser.parse_args(['test.png', '-i', self.testdir])
        compress(args)
        result = os.listdir(self.testdir)[1]
        expected = 'test_compressed.png'
        self.assertEqual(result, expected)

    def test_compresses_images_and_puts_in_output_dir(self):
        """
        Test function compresses images with filename, input dir and output dir
        args specified. Should also create the output dir if it doesn't exist.
        """
        args = self.parser.parse_args(
            ['test.png', '-i', self.testdir, '-o', self.outputdir])
        compress(args)
        result = os.listdir(self.outputdir)[0]
        expected = 'test.png'
        self.assertEqual(result, expected)

    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.testdir)

if __name__ == "__main__":
    unittest.main()
