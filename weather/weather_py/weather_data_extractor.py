from datetime import datetime, timedelta
from typing import List
from urllib.request import urlopen, urlretrieve
from zipfile import ZipFile

import os

from weather_py.util import open_read_close

weather_file_urls = [
    "http://cdn.knmi.nl/knmi/map/page/klimatologie/gegevens/uurgegevens/uurgeg_344_2001-2010.zip",
    "http://cdn.knmi.nl/knmi/map/page/klimatologie/gegevens/uurgegevens/uurgeg_344_2011-2020.zip"
]
LOCATION = "rotterdam"
_INDEXES = [-1] * 6
START_DATE = "20090101"  # YYYYMMDD of earliest report
END_DATE = "20111231"  # YYYYMMDD of last report


def download_files(urls=weather_file_urls) -> List[str]:
    """Downloads the weather files defined and extracts them so that we have a list of value(lists)"""
    data = []
    for url in urls:
        local_file, headers = urlretrieve(url)
        extracted_file_path = unzip_file(local_file)
        content = open_read_close(extracted_file_path[0])
        data.append(content)
    return data


def unzip_file(archive_file_path):
    print([archive_file_path, os.pardir], " .. ")
    target = os.path.abspath(os.path.join(archive_file_path, os.pardir))

    zfile = ZipFile(archive_file_path)
    contents = zfile.namelist()
    paths = [os.path.join(target, node) for node in contents]
    zfile.extractall(target)
    return paths


def get_indexes(line):
    parts = line.split(",")
    parts = list(map(lambda x: x.strip(), parts))
    _INDEXES[0] = parts.index("YYYYMMDD")  # date
    _INDEXES[1] = parts.index("HH")  # hour
    _INDEXES[2] = parts.index("DD")  # direction
    _INDEXES[3] = parts.index("FF")  # speed
    _INDEXES[4] = parts.index("T")  # temp
    _INDEXES[5] = parts.index("N")  # cover


def convert_weather_file(weather_data: str, start_date=START_DATE, end_date=END_DATE) -> List[List[str]]:
    lines = weather_data.split("\n")
    """converts the weather_data file content into a list of list of strings so we can work with it. It's the base data 
    that all other data is derived from 
    
    [0] date (datetime)
    [1] LOCATION (string)
    [2] temp (deg Celsius)
    [3] speed (m/s)
    [4] wind_dir (360deg)
    [5] cover ([0,1])
    
    """
    output_data = []
    prev_wind_dir = 0
    started = False

    for line in lines:
        if line.startswith("#"):
            started = True
            get_indexes(line)
            continue
        if len(line.strip()) == 0:
            continue
        if not started:
            continue

        parts = line.split(",")
        parts = [str.strip(part, " ") for part in parts]
        date = parts[_INDEXES[0]]
        hour = parts[_INDEXES[1]]
        wind_dir = parts[_INDEXES[2]]  # degrees
        speed = parts[_INDEXES[3]]  # 0.1 m/s
        temp = parts[_INDEXES[4]]  # 0.1 deg Celsius
        cover = parts[_INDEXES[5]] or "0"  # 0-9

        if date < start_date or date > end_date:
            continue

        hour = int(hour) - 1
        date = datetime.strptime(date, "%Y%m%d") + timedelta(hours=hour)
        wind_dir = int(wind_dir)
        speed = int(speed) / 10.0
        temp = int(temp) / 10.0
        cover = min(8, int(cover)) / 8.0

        if wind_dir == 0 or wind_dir > 360:
            wind_dir = prev_wind_dir
        wind_dir %= 360
        prev_wind_dir = wind_dir

        # insert data into dataset
        output_data.append([date, LOCATION, temp, speed, wind_dir, cover])

    return output_data
