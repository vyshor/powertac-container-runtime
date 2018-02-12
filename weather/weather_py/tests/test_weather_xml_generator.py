import unittest
from xml.dom.minidom import Document

import datetime

import weather_xml_generator as xg


class TestWeatherXmlGenerator(unittest.TestCase):

    def test_make_base_document(self):
        doc = xg.make_base_document()
        self.assertTrue(type(doc) == type(Document()))
        self.assertTrue(doc.hasChildNodes())
        self.assertEqual(len(doc.getElementsByTagName("data")), 1)

    def test_make_report_node(self):

        doc = Document()
        node = doc.createElement("weatherReport")
        input = [datetime.datetime(2009, 1, 1, 0, 0), 'rotterdam', -1.5, 1.0, 240, 1.0]
        xg.make_report_node(node, input)
        #print(node.toprettyxml(indent=""))

    @unittest.skip
    def test_make_data_document(self):
        """
        this tests the main generation of XML code for the offline server xml generation of weather data

        Based on these two Java Classes in the to be replaced Java App based approach
        https://github.com/powertac/powertac-weather-server/blob/master/src/main/java/org/powertac/weatherserver/beans/Weather.java
        https://github.com/powertac/powertac-weather-server/blob/master/src/main/java/org/powertac/weatherserver/beans/Forecast.java

        WEATHER
        =======
        private Double temp;
	    private Double windDir;
	    private Double windSpeed;
        private Double cloudCover;

        FORECAST (inherits from WEATHER)
        ========
        private int id = 0;
        private String origin;

        target xml nodes look like this

        <weatherForecast cloudcover="0.736" id="15" origin="2010-01-03 16:00" temp="-2.1" winddir="153" windspeed="2.27"/>
        <weatherReport   cloudcover="0.736" temp="-2.1" winddir="153" windspeed="2.27"/>
        """
        self.assertEqual(False, True)



