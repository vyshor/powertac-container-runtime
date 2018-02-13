from typing import List

import numpy as np
from datetime import datetime, timedelta

LOCATION = "rotterdam"
START_DATE = datetime.strptime("20090101", "%Y%m%d")
END_DATE = datetime.strptime("20111231", "%Y%m%d")
days = START_DATE - END_DATE

# FORECAST_SENSIBILITY = [2, 1, 10, 0.1]
FORECAST_SENSIBILITY = [2, 1, 10, 0.1]

DELTAS = [
    0.5162049085865681,
    0.5001617542505696,
    0.4895374321040051,
    0.4133156231642960,
    0.4254929262239113,
    0.4185106291938654,
    0.3936224626324226,
    0.3592021873751825,
    0.4227455362185202,
    0.2889786621257507,
    0.2990803149973352,
    0.2980053411248858,
    0.3278548743792022,
    0.3268537591678519,
    0.2222389153440853,
    0.2147271278862675,
    0.2271812561709724,
    0.2188789204055356,
    0.2534842863405704,
    0.1943563797606358,
    0.1769833979598591,
    0.1811455527733305,
    0.1341968742628301,
    0.1580705552864369,
]


def fill_to25_points(weather_rest: np.ndarray, points_left):
    """filling up an array of weather points with a repetition of the last item to allow for forecasts "past the end"
    with the simple rule of "will stay the same"
    """
    data = []
    data.extend(weather_rest)
    for i in range(points_left):
        data.append(weather_rest[-1])
    return np.array(data)


def make_forecasts(weather_data: np.ndarray) -> np.ndarray:
    """ We need 1094 days, with 24 forecasts for each hour slot. Each 24h forecasts per timeslot are dependent on the
    following 24h of weather measurements and some iteratively calculated error deviation that is based on the DELTAS
    :param weather_data: a list of raw weather data points. For each point, a 24 item long array of forecasts for the future will be created
    """

    # our array of forecasts. This is a --- days * 24h X 24h X forecast_tuple data structure
    all_fc = np.empty((len(weather_data), 24), dtype=object)

    for i in range(len(weather_data)):
        # skipping last day of forecasting for now TODO improve
        if i > len(weather_data):
            continue
        if i+25 > len(weather_data):
            points_left = i+25-len(weather_data)
            d = fill_to25_points(weather_data[i:], points_left)
            all_fc[i] = make_24h_forecasts(d)
        else:
            all_fc[i] = make_24h_forecasts(weather_data[i:i+25])
    return all_fc


def make_24h_forecasts(weather: np.ndarray) -> List[List]:
    """
    Creates 24h of forecasts for the first item in the array based on the following 24.

    INGOING --> measurements
    [0] date (datetime)
    [1] LOCATION (string)
    [2] temp (deg Celsius)
    [3] speed (m/s)
    [4] wind_dir (360deg)
    [5] cover ([0,1])

    OUTGOING --> forecasts
    [0] date (datetime)
    [1] LOCATION (string)
    [2] temp (deg Celsius)
    [3] speed (m/s)
    [4] wind_dir (360deg)
    [5] cover ([0,1])
    [6] origin (datetime)

    :param weather: a 25 item long array of weather data
    :return:
    """
    forecast_length = len(weather)-1

    forecasts = np.zeros((4, forecast_length))
    fc_list = []
    taus = np.zeros((4, forecast_length))
    for i in range(forecast_length):
        # generating [4,24] matrix of deviations
        fill_taus(i, taus)

        forecasts[:4, i] = weather[i + 1, 2:] + FORECAST_SENSIBILITY * + taus[:, i]    # filling forecasts matrix

        forecasts[1, i]  = max(min(forecasts[1, i], 19), 0)                     # speed correction
        forecasts[2, i]  = int((forecasts[2, i]) % 360)                         # wind direction correction
        forecasts[3, i]  = max(min(forecasts[3, i], 1), 0)                      # cloud cover correction
        fc_list.append(merge_forecast_data(forecasts[:, i], weather[i + 1, 0], weather[0, 0]))
    return fc_list


def fill_taus(i, taus):
    if i == 0:
        taus[:, i] = np.zeros(4) + np.random.normal(0, DELTAS[i], 4)
    else:
        taus[:, i] = taus[:, i - 1] + np.random.normal(0, DELTAS[i], 4)


def merge_forecast_data(forecasts, date, origin):
    tup = [date, LOCATION]
    tup.extend(forecasts)
    tup.append(origin)
    return tup
