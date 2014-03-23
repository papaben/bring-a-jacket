"""
Checks the weather for you
"""
import forecastio
from dr_rain_configs import DrRainConfigs

_configs = DrRainConfigs()

_api_key = _configs.weather_api_key()


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
