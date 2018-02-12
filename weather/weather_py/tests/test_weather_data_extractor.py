import unittest

import os

from util import open_read_close
from weather_py import weather_data_extractor as we


class TestWeatherDataExtractor(unittest.TestCase):

    @unittest.skip
    def test_download_files(self):
        # archive_path = os.path.join(get_file_dir(), "testarchive.zip")
        url = "http://cdn.knmi.nl/knmi/map/page/klimatologie/gegevens/uurgegevens/uurgeg_344_2001-2010.zip"
        files = we.download_files([url])

        self.assertEqual(len(files), 1)
        self.assertEqual(files[0][0:4], "BRON")

    def test_unzip_file(self):
        archive_file_path = os.path.join(get_file_dir(), "testarchive.zip")
        extracted_file_path = os.path.join(get_file_dir(), "testfile.txt")
        data = we.unzip_file(archive_file_path)
        self.assertEqual(data[0], extracted_file_path)

        # cleanup
        os.remove(extracted_file_path)

    def test_convert_weather_file(self):
        test_data = open_read_close(os.path.join(get_file_dir(), "testdata.txt"))
        output = we.convert_weather_file(test_data)
        self.assertEqual(len(output), 1000)
        for entry in output[0:20]:
            self.assertEqual(len(entry), 6)



def get_file_dir() -> str:
    return os.path.dirname(os.path.realpath(__file__))
