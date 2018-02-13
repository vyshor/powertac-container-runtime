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
FC_TAG_NAME = "weatherForecasts"
WR_TAG_NAME = "weatherReports"
ER_TAG_NAME = "energyReports"


def make_data_document(forecasts, reports) -> Document:
    # make doc
    doc = make_base_document()
    fc_node = doc.getElementsByTagName(FC_TAG_NAME)[0]
    wr_node = doc.getElementsByTagName(WR_TAG_NAME)[0]

    # generate nodes for data
    xwr_list = [make_report_node(doc.createElement("weatherReport"), r) for r in reports]
    xfc_list = [make_forecast_node(doc.createElement("weatherForecast"), fc) for fc in forecasts]

    # put them all in the doc
    for xfc in xfc_list:
        fc_node.appendChild(xfc)
    for xwr in xwr_list:
        wr_node.appendChild(xwr)

    return doc


def make_base_document() -> Document:
    doc = Document()

    root_element = doc.createElement('data')

    fc_node = doc.createElement(FC_TAG_NAME)
    wr_node = doc.createElement(WR_TAG_NAME)
    er_node = doc.createElement(ER_TAG_NAME)
    root_element.appendChild(fc_node)
    root_element.appendChild(wr_node)
    root_element.appendChild(er_node)

    doc.appendChild(root_element)
    return doc


def make_report_node(elem: Element, data: List):
    date = data[0].isoformat(sep=' ', timespec='minutes')
    temp = '{0:.1f}'.format(data[2])  # 1 decimal precision
    windspeed = '{0:.2f}'.format(data[3])  # 2 decimal precision
    winddir = '{}'.format(round(data[4]))
    cloudcover = '{0:.3f}'.format(data[5])

    elem.setAttribute('date', date)
    elem.setAttribute('location', data[1])
    elem.setAttribute('temp', temp)
    elem.setAttribute('windspeed', windspeed)
    elem.setAttribute('winddir', winddir)
    elem.setAttribute('cloudcover', cloudcover)
    return elem


def make_forecast_node(elem: Element, data: List) -> Element:
    elem = make_report_node(elem, data)

    origin = data[6].isoformat(sep=' ', timespec='minutes')
    elem.setAttribute('origin', origin)
    return elem


def make_date_based_dict(li: List):
    d = {}

    for val in li:
        key = val[0]
        if key not in d:
            d[key] = []
        d[key].append(val)
    return d
