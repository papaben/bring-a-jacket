"""
Send emails from Dr. Rain
"""
__author__ = 'slartibart'


import smtplib


_initialized = False
_username = 'bring.a.jacket@gmail.com'


def _get_server():
    """
    Memoize connection to mail server
    """
    if not _initialized:
        # Reduce open connections by sharing a single server object
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        password = 'DrKnock#rs'
        server.login(_username, password)

        _initialized = True

    return server


def send_it_will_rain_email(probability, to_addr):
    """
    Send an email about the rain
    :param probability: string
    :param to_addr: string
    """
    msg = "\r\n".join([
        "From: Dr. Rain <" + _username + ">",
        "To: " + to_addr,
        "Subject: Rain in the Forecast! ({0})".format(probability),
        "",
        "Rain probability is {0}. You'd better bring a jacket.".format(probability)
    ])

    _get_server().sendmail(_username, [to_addr], msg)


def close():
    """
    Close active connection to mail server
    """
    if _initialized:
        _get_server().quit()

