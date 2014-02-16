__author__ = 'slartibart'

import forecastio
import smtplib


def send_it_will_rain_email(probability):
    """
    Send me an email warning about the rain
    @type probability: string
    """
    fromaddr = 'bring.a.jacket@gmail.com'
    toaddr = 'vanevery@gmail.com'
    username = 'bring.a.jacket@gmail.com'
    password = 'DrKnock#rs'
    msg = "\r\n".join([
        "From: Dr. Rain <" + fromaddr + ">",
        "To: " + toaddr,
        "Subject: Rain in the Forecast!",
        "",
        "Rain probability is {0}. You'd better bring a jacket.".format(probability)
    ])
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, [toaddr], msg)
    server.quit()


def alert_if_tomorrow_is_rainy(daily_forecast):
    """
    Determines if it will rain tomorrow
    @type daily_forecast: ForecastioDataBlock
    """

    tomorrow = daily_forecast.data.pop(1)

    print("Got data for tomorrow")

    if tomorrow.precipProbability > 0.5:
        print("Probably will rain tomorrow; sending email")
        send_it_will_rain_email(prob_to_percent(tomorrow.precipProbability))


def prob_to_percent(probability):
    """
    Convert probability to a percentage
    :type probability: float Decimal value between 0 and 1
    :rtype: string Probability as percentage
    """
    return "{0}%".format(int(probability * 100))


if __name__ == "__main__":
    api_key = "4d6b83422b6dc943be406ffcb44376bc"

    lat = 37.4828
    lng = -122.2361
    # https://api.forecast.io/forecast/4d6b83422b6dc943be406ffcb44376bc/37.4828,-122.2361
    forecast = forecastio.load_forecast(api_key, lat, lng)

    daily = forecast.daily()
    alert_if_tomorrow_is_rainy(daily)


