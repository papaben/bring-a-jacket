"""
Checks the weather for you
"""
__author__ = 'slartibart'

import forecastio

_api_key = "4d6b83422b6dc943be406ffcb44376bc"


def tomorrow(lat, lng):
    """
    Returns tomorrow's weather
    :param lat:
    :param lng:
    :return:
    """
    # TODO memoize by lat and lng?
    forecast = forecastio.load_forecast(_api_key, lat, lng)

    daily_forecasts = forecast.daily()
    return daily_forecasts.data.pop(1)
