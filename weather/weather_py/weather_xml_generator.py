"""
This script produces a weatherfile for running an offline or repeated sim
"""

from datetime import datetime, timedelta
import urllib
import sys
from typing import List
from xml.dom import minidom
from xml.dom.minidom import Document, Element

DAYS = 794
LOCATION = "rotterdam"


# LOCATION = "minneapolis"


def make_data_document() -> Document:
    doc = make_base_document()
    return None


def make_base_document() -> Document:
    doc = Document()

    root_element = doc.createElement('data')

    doc.appendChild(root_element)
    return doc


def make_report_node(elem: Element, report_list: List[str]):
    elem.setAttribute("temp", str(report_list[2]))
    elem.setAttribute("windspeed", str(report_list[3]))
    elem.setAttribute("winddir", str(report_list[4]))
    elem.setAttribute("cloudcover", str(report_list[5]))

def make_forecast_node(elem: Element, forecast_data: List[str]):
    return None