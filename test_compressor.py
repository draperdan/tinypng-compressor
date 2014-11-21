import unittest
import tempfile
import shutil
import os
from PIL import Image
from compressor import compress
import sys


class TestCompressor(unittest.TestCase):

    def setUp(self):
        self.origdir = os.getcwd()
        self.testdir = tempfile.mkdtemp('tempdir')
        os.chdir(self.testdir)
        self.image = Image.new('RGB', (100, 100), 'white')
        self.image.save('test.png')
        self.image.close()
        self.command_line_arg = sys.argv = ['-d', self.testdir]

    def test_compresser_returns_compressed_file(self):
        """
        Compresses mock image and matches file name against
        expected file name.
        """
        compress(self.command_line_arg)
        compressed_file = os.listdir(self.testdir)[1]
        expected = 'test_tny.png'
        self.assertEqual(compressed_file, expected)

    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.testdir)

if __name__ == "__main__":
    unittest.main()
