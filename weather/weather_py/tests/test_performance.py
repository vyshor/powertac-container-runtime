import timeit
import unittest

import numpy as np

import forecast_generator as fg
import weather_data_extractor as we
import weather_xml_generator as mx
from tests import test_forecast_generator as tfg

class TestPerformance:
    @unittest.skip
    def _test_simulation_generation_perf(self):
        """
        test function to see how fast we can generate all of our simulations
        :return:
        """

        timeit_setup = '''
import forecast_generator as fg
from tests import test_forecast_generator as tfg
import numpy as np

data = tfg.TEST_WEATHER_VALUES[0:25]
data = np.array(data)
        '''
        print(
            "Testing performance for creating {} forecasts based on {} weather_points".format(25 * 24 * 100, 25 * 100))
        print("The test is run 7 times and then the best result is taken")
        print(min(timeit.Timer('a = fg.make_forecasts(data)', setup=timeit_setup).repeat(7, 100)))

