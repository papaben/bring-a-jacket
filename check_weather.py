"""
The main script that kicks things off
"""

import dr_rain
import logging
import weather_man


def alert_if_tomorrow_is_rainy(lat, lng):
    """
    Send email if P(rain tomorrow) > threshold
    """
    tomorrow = weather_man.tomorrow(lat, lng)
    probability = tomorrow.precipProbability
    threshold = 0.5

    _logger.debug("Tomorrow's probability is {0}.".format(probability))
    if probability > threshold:
        _logger.info("Sending email for P(rain) {0} > threshold {1}".format(probability, threshold))
        dr_rain.send_it_will_rain_email(prob_to_percent(probability), "vanevery@gmail.com")


def prob_to_percent(probability):
    """
    Convert probability to a percentage
    :type probability: float Decimal value between 0 and 1
    :rtype: string Probability as percentage
    """
    return "{0}%".format(int(probability * 100))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    _logger = logging.getLogger(__name__)

    lat = 37.4828
    lng = -122.2361

    alert_if_tomorrow_is_rainy(lat, lng)
    dr_rain.close()

    # Plan:
    # ----
    # For a given person,
    # * lat,long
    # * threshold
    # ...notification method(s)

