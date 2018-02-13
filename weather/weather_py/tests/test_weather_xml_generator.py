import unittest
from xml.dom.minidom import Document

import datetime

import weather_xml_generator as xg
from tests import test_forecast_generator


class TestWeatherXmlGenerator(unittest.TestCase):

    def test_make_base_document(self):
        doc = xg.make_base_document()
        self.assertTrue(type(doc) == type(Document()))
        self.assertTrue(doc.hasChildNodes())
        self.assertEqual(len(doc.getElementsByTagName("data")), 1)

    def test_make_forecast_node(self):
        expect = '<weatherForecast cloudcover="1.000" date="2009-01-01 01:00" location="rotterdam" '\
                 'origin="2009-01-01 00:00" temp="-1.7" winddir="278" windspeed="0.77"/>'
        input = TEST_FORECAST_VALUES[0]
        element = Document().createElement("weatherForecast")
        xml = xg.make_forecast_node(element, input)
        self.assertEqual(expect, xml.toprettyxml().strip())  # prettyprint gives \n at end of string


    def test_make_report_node(self):
        expect = '<weatherReport cloudcover="1.000" date="2009-01-01 01:00" location="rotterdam" ' \
                 'temp="-1.7" winddir="278" windspeed="0.77"/>'
        doc = Document()
        node = doc.createElement("weatherReport")
        input = TEST_FORECAST_VALUES[0]
        xml = xg.make_report_node(node, input)
        self.assertEqual(expect, xml.toprettyxml().strip())

    def test_make_date_based_dict(self):
        list = []
        list.extend(TEST_FORECAST_VALUES)
        list.extend(test_forecast_generator.TEST_WEATHER_VALUES)


        dict = xg.make_date_based_dict(list)
        key = TEST_FORECAST_VALUES[0][0]
        self.assertEqual(2, len(dict[key]))
        self.assertEqual(100, len(dict.keys()))

    #@unittest.skip
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

        It's unclear how exactly the xml is returned by the server, but the query form (by date and location) suggests each day is returned as a report + all its forecasts
        """
        forecasts = TEST_FORECAST_VALUES
        reports = test_forecast_generator.TEST_WEATHER_VALUES[0:24]
        doc = xg.make_data_document(forecasts, reports)

        self.assertEqual(len(forecasts), len(doc.getElementsByTagName("weatherForecast")))
        self.assertEqual(len(reports), len(doc.getElementsByTagName("weatherReport")))



TEST_FORECAST_VALUES = [list([datetime.datetime(2009, 1, 1, 1, 0), 'rotterdam', -1.7313036128051986, 0.7679377872310553, 278.0, 1.0, datetime.datetime(2009, 1, 1, 0, 0)]),
  list([datetime.datetime(2009, 1, 1, 2, 0), 'rotterdam', -1.6051557610454563, 1.8081412713328788, 244.0, 1.0, datetime.datetime(2009, 1, 1, 0, 0)]),
  list([datetime.datetime(2009, 1, 1, 3, 0), 'rotterdam', -1.8441383368745121, 1.2820550557092334, 258.0, 0.8962187383111403, datetime.datetime(2009, 1, 1, 0, 0)]),
  list([datetime.datetime(2009, 1, 1, 4, 0), 'rotterdam', -0.9583431189741556, 1.5044967823128577, 256.0, 0.9189855025543954, datetime.datetime(2009, 1, 1, 0, 0)]),
  list([datetime.datetime(2009, 1, 1, 5, 0), 'rotterdam', -1.7047208112876313, 2.0251980092118202, 255.0, 0.8570402583606399, datetime.datetime(2009, 1, 1, 0, 0)]),
  list([datetime.datetime(2009, 1, 1, 6, 0), 'rotterdam', -0.7931608530446157, 1.3047204797690934, 315.0, 0.893463003313317, datetime.datetime(2009, 1, 1, 0, 0)]),
  list([datetime.datetime(2009, 1, 1, 7, 0), 'rotterdam', -1.7894555351274644, 0.7517482404551524, 314.0, 0.9313564641564738, datetime.datetime(2009, 1, 1, 0, 0)]),
  list([datetime.datetime(2009, 1, 1, 8, 0), 'rotterdam', -1.1016208428434742, 2.2554535774387454, 182.0, 0.9086001924863618, datetime.datetime(2009, 1, 1, 0, 0)]),
  list([datetime.datetime(2009, 1, 1, 9, 0), 'rotterdam', -0.6923506785920794, 1.9359574057158335, 201.0, 0.8508234944136455, datetime.datetime(2009, 1, 1, 0, 0)]),
  list([datetime.datetime(2009, 1, 1, 10, 0), 'rotterdam', 0.12668797490003214, 1.7924936666816111, 262.0, 0.8199434024137159, datetime.datetime(2009, 1, 1, 0, 0)]),
  list([datetime.datetime(2009, 1, 1, 11, 0), 'rotterdam', 1.8199823609335735, 2.1007978603347874, 256.0, 0.8078031033920153, datetime.datetime(2009, 1, 1, 0, 0)]),
  list([datetime.datetime(2009, 1, 1, 12, 0), 'rotterdam', 1.6991478209808335, 1.9557311261894372, 242.0, 0.8171166985448635, datetime.datetime(2009, 1, 1, 0, 0)]),
  list([datetime.datetime(2009, 1, 1, 13, 0), 'rotterdam', 3.025248644931138, 0.733050548774934, 309.0, 0.7803740111669172, datetime.datetime(2009, 1, 1, 0, 0)]),
  list([datetime.datetime(2009, 1, 1, 14, 0), 'rotterdam', 2.8870785639151713, 0.6693582572536435, 231.0, 0.7743577235186431, datetime.datetime(2009, 1, 1, 0, 0)]),
  list([datetime.datetime(2009, 1, 1, 15, 0), 'rotterdam', 2.880553947510136, 1.8457567535415584, 251.0, 0.782812958899724, datetime.datetime(2009, 1, 1, 0, 0)]),
  list([datetime.datetime(2009, 1, 1, 16, 0), 'rotterdam', 2.5994377020753663, 1.03664299313813, 254.0, 0.7963484476023841, datetime.datetime(2009, 1, 1, 0, 0)]),
  list([datetime.datetime(2009, 1, 1, 17, 0), 'rotterdam', 2.168549888012178, 2.0462388236506954, 224.0, 0.7668139822373486, datetime.datetime(2009, 1, 1, 0, 0)]),
  list([datetime.datetime(2009, 1, 1, 18, 0), 'rotterdam', 2.6985110721323013, 1.232479663487176, 231.0, 0.7551118524585508, datetime.datetime(2009, 1, 1, 0, 0)]),
  list([datetime.datetime(2009, 1, 1, 19, 0), 'rotterdam', 2.8316985952493585, 2.2508748640406293, 209.0, 0.7614590862377248, datetime.datetime(2009, 1, 1, 0, 0)]),
  list([datetime.datetime(2009, 1, 1, 20, 0), 'rotterdam', 2.7940382359302376, 2.244645269567929, 222.0, 0.7774394399312161, datetime.datetime(2009, 1, 1, 0, 0)]),
  list([datetime.datetime(2009, 1, 1, 21, 0), 'rotterdam', 3.229137346357781, 4.2385511081928975, 234.0, 0.8009648471933686, datetime.datetime(2009, 1, 1, 0, 0)]),
  list([datetime.datetime(2009, 1, 1, 22, 0), 'rotterdam', 3.1390404160467913, 2.2755895746286208, 224.0, 0.8020062146417478, datetime.datetime(2009, 1, 1, 0, 0)]),
  list([datetime.datetime(2009, 1, 1, 23, 0), 'rotterdam', 2.9801544652912777, 2.1172100832302885, 262.0, 0.828809802483878, datetime.datetime(2009, 1, 1, 0, 0)]),
  list([datetime.datetime(2009, 1, 2, 0, 0), 'rotterdam', 3.203932821127437, 2.291689766955645, 253.0, 0.8464481592265533, datetime.datetime(2009, 1, 1, 0, 0)])]