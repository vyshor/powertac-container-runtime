import pprint
import unittest
import datetime
import numpy as np
import forecast_generator as fg

TEST_SEED = 1234567


class TestForecastGenerator(unittest.TestCase):

    def setUp(self):
        np.random.seed(TEST_SEED)

    #@unittest.skip
    def test_make_forecasts(self):
        forecasts = fg.make_forecasts(TEST_WEATHER_VALUES)
        self.assertEqual(len(TEST_WEATHER_VALUES), len(forecasts))
        self.assertTrue(forecasts[-1].all())
        self.assertTrue(type(forecasts[0] is np.ndarray))

    def test_fill_to25_points(self):
        weather_rest = TEST_WEATHER_VALUES[0:10]
        points_left = 25-len(weather_rest)
        weather_values = fg.fill_to25_points(weather_rest, points_left)
        self.assertEqual(len(weather_values), 25)
        # assert same date for the filled up values
        self.assertEqual(weather_values[-1][0], weather_values[10][0])

        # should also work with just one item
        just_one = TEST_WEATHER_VALUES[0:1]
        points_left = 25 - len(just_one)
        weather_values = fg.fill_to25_points(just_one, points_left)
        self.assertEqual(len(weather_values), 25)
        # assert same date for the filled up values
        self.assertEqual(weather_values[-1][0], weather_values[0][0])

    def test_make_24h_forecasts(self):
        values_ = TEST_WEATHER_VALUES[0:25]
        self.assertEqual(25, len(values_))
        self.assertEqual(6, len(values_[0]))


        forecasts = fg.make_24h_forecasts(values_)

        # expect no errors with different number of forecast distances
        ten_fc = fg.make_24h_forecasts(TEST_WEATHER_VALUES[0:11])
        self.assertEqual(10, len(ten_fc))
        # but expect an error on over 24 --> the DELTAS aren't sufficient for that
        self.assertRaises(IndexError, fg.make_24h_forecasts, TEST_WEATHER_VALUES[0:34])

        # expect good values on calls with 25 values (1 for current date + the future 24 weather values
        self.assertEqual(24, len(forecasts))
        self.assertEqual(7, len(forecasts[0]))



    def test_merge_forecast_data(self):
        forecasts = TEST_WEATHER_VALUES[1, 2:]
        origin = TEST_WEATHER_VALUES[0, 0]
        date = TEST_WEATHER_VALUES[1, 0]
        forecast_item = fg.merge_forecast_data(forecasts, date, origin)
        self.assertEqual(7, len(forecast_item))
        self.assertTrue(type(forecast_item[0] is datetime.datetime))
        self.assertTrue(type(forecast_item[1] is str))
        self.assertTrue(type(forecast_item[2] is float))
        self.assertTrue(type(forecast_item[6] is datetime.datetime))


TEST_WEATHER_VALUES = np.array([[datetime.datetime(2009, 1, 1, 0, 0), 'rotterdam', -1.5, 1.0, 240, 1.0],
                                [datetime.datetime(2009, 1, 1, 1, 0), 'rotterdam', -1.2, 1.0, 270, 1.0],
                                [datetime.datetime(2009, 1, 1, 2, 0), 'rotterdam', -1.1, 2.0, 240, 1.0],
                                [datetime.datetime(2009, 1, 1, 3, 0), 'rotterdam', -1.0, 1.0, 250, 1.0],
                                [datetime.datetime(2009, 1, 1, 4, 0), 'rotterdam', -0.9, 1.0, 250, 1.0],
                                [datetime.datetime(2009, 1, 1, 5, 0), 'rotterdam', -1.0, 1.0, 250, 1.0],
                                [datetime.datetime(2009, 1, 1, 6, 0), 'rotterdam', -1.1, 1.0, 310, 1.0],
                                [datetime.datetime(2009, 1, 1, 7, 0), 'rotterdam', -1.1, 1.0, 310, 1.0],
                                [datetime.datetime(2009, 1, 1, 8, 0), 'rotterdam', -0.5, 2.0, 180, 1.0],
                                [datetime.datetime(2009, 1, 1, 9, 0), 'rotterdam', -0.4, 2.0, 200, 1.0],
                                [datetime.datetime(2009, 1, 1, 10, 0), 'rotterdam', -0.3, 2.0, 260, 1.0],
                                [datetime.datetime(2009, 1, 1, 11, 0), 'rotterdam', -0.3, 2.0, 260, 1.0],
                                [datetime.datetime(2009, 1, 1, 12, 0), 'rotterdam', 0.0, 2.0, 240, 1.0],
                                [datetime.datetime(2009, 1, 1, 13, 0), 'rotterdam', 0.2, 1.0, 310, 1.0],
                                [datetime.datetime(2009, 1, 1, 14, 0), 'rotterdam', -0.1, 1.0, 230, 1.0],
                                [datetime.datetime(2009, 1, 1, 15, 0), 'rotterdam', 0.0, 2.0, 250, 1.0],
                                [datetime.datetime(2009, 1, 1, 16, 0), 'rotterdam', -0.2, 1.0, 250, 1.0],
                                [datetime.datetime(2009, 1, 1, 17, 0), 'rotterdam', 0.0, 2.0, 220, 1.0],
                                [datetime.datetime(2009, 1, 1, 18, 0), 'rotterdam', 0.0, 1.0, 230, 1.0],
                                [datetime.datetime(2009, 1, 1, 19, 0), 'rotterdam', 0.2, 2.0, 210, 1.0],
                                [datetime.datetime(2009, 1, 1, 20, 0), 'rotterdam', 0.2, 2.0, 220, 1.0],
                                [datetime.datetime(2009, 1, 1, 21, 0), 'rotterdam', 0.4, 4.0, 230, 1.0],
                                [datetime.datetime(2009, 1, 1, 22, 0), 'rotterdam', 0.4, 2.0, 220, 1.0],
                                [datetime.datetime(2009, 1, 1, 23, 0), 'rotterdam', 0.4, 2.0, 260, 1.0],
                                [datetime.datetime(2009, 1, 2, 0, 0), 'rotterdam', 0.7, 2.0, 250, 1.0],
                                [datetime.datetime(2009, 1, 2, 1, 0), 'rotterdam', 0.6, 2.0, 240, 1.0],
                                [datetime.datetime(2009, 1, 2, 2, 0), 'rotterdam', 0.8, 1.0, 320, 0.875],
                                [datetime.datetime(2009, 1, 2, 3, 0), 'rotterdam', 0.5, 1.0, 220, 1.0],
                                [datetime.datetime(2009, 1, 2, 4, 0), 'rotterdam', 1.4, 2.0, 290, 1.0],
                                [datetime.datetime(2009, 1, 2, 5, 0), 'rotterdam', 1.8, 3.0, 340, 1.0],
                                [datetime.datetime(2009, 1, 2, 6, 0), 'rotterdam', 1.8, 2.0, 350, 1.0],
                                [datetime.datetime(2009, 1, 2, 7, 0), 'rotterdam', 1.5, 1.0, 340, 1.0],
                                [datetime.datetime(2009, 1, 2, 8, 0), 'rotterdam', 1.6, 2.0, 40, 1.0],
                                [datetime.datetime(2009, 1, 2, 9, 0), 'rotterdam', 2.1, 2.0, 30, 1.0],
                                [datetime.datetime(2009, 1, 2, 10, 0), 'rotterdam', 3.0, 5.0, 40, 1.0],
                                [datetime.datetime(2009, 1, 2, 11, 0), 'rotterdam', 2.3, 6.0, 50, 1.0],
                                [datetime.datetime(2009, 1, 2, 12, 0), 'rotterdam', 1.8, 6.0, 40, 1.0],
                                [datetime.datetime(2009, 1, 2, 13, 0), 'rotterdam', 0.8, 5.0, 60, 1.0],
                                [datetime.datetime(2009, 1, 2, 14, 0), 'rotterdam', 0.5, 4.0, 70, 1.0],
                                [datetime.datetime(2009, 1, 2, 15, 0), 'rotterdam', -0.4, 3.0, 40, 0.0],
                                [datetime.datetime(2009, 1, 2, 16, 0), 'rotterdam', -2.1, 3.0, 60, 0.0],
                                [datetime.datetime(2009, 1, 2, 17, 0), 'rotterdam', -1.6, 3.0, 50, 0.0],
                                [datetime.datetime(2009, 1, 2, 18, 0), 'rotterdam', -2.6, 2.0, 50, 0.0],
                                [datetime.datetime(2009, 1, 2, 19, 0), 'rotterdam', -2.3, 2.0, 60, 0.0],
                                [datetime.datetime(2009, 1, 2, 20, 0), 'rotterdam', -3.8, 1.0, 40, 0.0],
                                [datetime.datetime(2009, 1, 2, 21, 0), 'rotterdam', -4.3, 1.0, 30, 0.0],
                                [datetime.datetime(2009, 1, 2, 22, 0), 'rotterdam', -4.8, 1.0, 40, 0.0],
                                [datetime.datetime(2009, 1, 2, 23, 0), 'rotterdam', -5.9, 1.0, 30, 0.0],
                                [datetime.datetime(2009, 1, 3, 0, 0), 'rotterdam', -7.6, 1.0, 0, 0.0],
                                [datetime.datetime(2009, 1, 3, 1, 0), 'rotterdam', -6.8, 0.0, 0, 0.0],
                                [datetime.datetime(2009, 1, 3, 2, 0), 'rotterdam', -7.8, 1.0, 10, 0.0],
                                [datetime.datetime(2009, 1, 3, 3, 0), 'rotterdam', -8.6, 1.0, 160, 0.0],
                                [datetime.datetime(2009, 1, 3, 4, 0), 'rotterdam', -8.2, 1.0, 300, 0.25],
                                [datetime.datetime(2009, 1, 3, 5, 0), 'rotterdam', -8.8, 0.0, 300, 1.0],
                                [datetime.datetime(2009, 1, 3, 6, 0), 'rotterdam', -8.1, 1.0, 300, 1.0],
                                [datetime.datetime(2009, 1, 3, 7, 0), 'rotterdam', -7.4, 1.0, 300, 1.0],
                                [datetime.datetime(2009, 1, 3, 8, 0), 'rotterdam', -5.1, 1.0, 300, 1.0],
                                [datetime.datetime(2009, 1, 3, 9, 0), 'rotterdam', -2.4, 1.0, 210, 1.0],
                                [datetime.datetime(2009, 1, 3, 10, 0), 'rotterdam', -1.2, 2.0, 220, 1.0],
                                [datetime.datetime(2009, 1, 3, 11, 0), 'rotterdam', -0.1, 3.0, 230, 1.0],
                                [datetime.datetime(2009, 1, 3, 12, 0), 'rotterdam', 0.3, 2.0, 240, 1.0],
                                [datetime.datetime(2009, 1, 3, 13, 0), 'rotterdam', 0.4, 4.0, 230, 1.0],
                                [datetime.datetime(2009, 1, 3, 14, 0), 'rotterdam', 0.5, 4.0, 230, 1.0],
                                [datetime.datetime(2009, 1, 3, 15, 0), 'rotterdam', 0.7, 3.0, 220, 1.0],
                                [datetime.datetime(2009, 1, 3, 16, 0), 'rotterdam', 0.8, 4.0, 230, 1.0],
                                [datetime.datetime(2009, 1, 3, 17, 0), 'rotterdam', 0.7, 3.0, 230, 1.0],
                                [datetime.datetime(2009, 1, 3, 18, 0), 'rotterdam', 0.5, 3.0, 220, 1.0],
                                [datetime.datetime(2009, 1, 3, 19, 0), 'rotterdam', 1.5, 2.0, 250, 1.0],
                                [datetime.datetime(2009, 1, 3, 20, 0), 'rotterdam', 0.8, 2.0, 220, 1.0],
                                [datetime.datetime(2009, 1, 3, 21, 0), 'rotterdam', 1.1, 2.0, 230, 1.0],
                                [datetime.datetime(2009, 1, 3, 22, 0), 'rotterdam', 1.9, 2.0, 280, 1.0],
                                [datetime.datetime(2009, 1, 3, 23, 0), 'rotterdam', 2.3, 3.0, 290, 1.0],
                                [datetime.datetime(2009, 1, 4, 0, 0), 'rotterdam', 2.4, 4.0, 290, 1.0],
                                [datetime.datetime(2009, 1, 4, 1, 0), 'rotterdam', 2.3, 4.0, 290, 1.0],
                                [datetime.datetime(2009, 1, 4, 2, 0), 'rotterdam', 1.9, 6.0, 290, 1.0],
                                [datetime.datetime(2009, 1, 4, 3, 0), 'rotterdam', 1.6, 4.0, 260, 1.0],
                                [datetime.datetime(2009, 1, 4, 4, 0), 'rotterdam', 1.8, 5.0, 270, 1.0],
                                [datetime.datetime(2009, 1, 4, 5, 0), 'rotterdam', 1.8, 4.0, 270, 1.0],
                                [datetime.datetime(2009, 1, 4, 6, 0), 'rotterdam', 2.2, 5.0, 260, 1.0],
                                [datetime.datetime(2009, 1, 4, 7, 0), 'rotterdam', 2.3, 4.0, 260, 1.0],
                                [datetime.datetime(2009, 1, 4, 8, 0), 'rotterdam', 2.6, 4.0, 260, 1.0],
                                [datetime.datetime(2009, 1, 4, 9, 0), 'rotterdam', 2.9, 4.0, 260, 1.0],
                                [datetime.datetime(2009, 1, 4, 10, 0), 'rotterdam', 3.5, 5.0, 260, 1.0],
                                [datetime.datetime(2009, 1, 4, 11, 0), 'rotterdam', 3.6, 4.0, 260, 1.0],
                                [datetime.datetime(2009, 1, 4, 12, 0), 'rotterdam', 3.7, 5.0, 270, 1.0],
                                [datetime.datetime(2009, 1, 4, 13, 0), 'rotterdam', 3.5, 6.0, 270, 1.0],
                                [datetime.datetime(2009, 1, 4, 14, 0), 'rotterdam', 3.3, 5.0, 270, 1.0],
                                [datetime.datetime(2009, 1, 4, 15, 0), 'rotterdam', 3.1, 4.0, 260, 1.0],
                                [datetime.datetime(2009, 1, 4, 16, 0), 'rotterdam', 3.1, 4.0, 270, 1.0],
                                [datetime.datetime(2009, 1, 4, 17, 0), 'rotterdam', 2.9, 5.0, 280, 1.0],
                                [datetime.datetime(2009, 1, 4, 18, 0), 'rotterdam', 2.4, 4.0, 280, 1.0],
                                [datetime.datetime(2009, 1, 4, 19, 0), 'rotterdam', 2.3, 4.0, 270, 1.0],
                                [datetime.datetime(2009, 1, 4, 20, 0), 'rotterdam', 2.0, 4.0, 270, 1.0],
                                [datetime.datetime(2009, 1, 4, 21, 0), 'rotterdam', 2.2, 5.0, 260, 1.0],
                                [datetime.datetime(2009, 1, 4, 22, 0), 'rotterdam', 2.0, 4.0, 260, 1.0],
                                [datetime.datetime(2009, 1, 4, 23, 0), 'rotterdam', 2.1, 5.0, 260, 1.0],
                                [datetime.datetime(2009, 1, 5, 0, 0), 'rotterdam', 2.2, 5.0, 260, 1.0],
                                [datetime.datetime(2009, 1, 5, 1, 0), 'rotterdam', 2.5, 6.0, 240, 1.0],
                                [datetime.datetime(2009, 1, 5, 2, 0), 'rotterdam', 0.9, 6.0, 70, 1.0],
                                [datetime.datetime(2009, 1, 5, 3, 0), 'rotterdam', 0.7, 7.0, 50, 1.0]])
