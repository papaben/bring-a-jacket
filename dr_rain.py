"""
Notifies people of weather
"""
__author__ = 'slartibart'


import smtplib


_server = smtplib.SMTP('smtp.gmail.com:587')
_server.ehlo()
_server.starttls()
_username = 'bring.a.jacket@gmail.com'
_password = 'DrKnock#rs'
_server.login(_username, _password)


def send_it_will_rain_email(probability, toaddr):
    """
    Send an email warning about the rain
    :param probability: string
    :param toaddr: string
    """
    fromaddr = 'bring.a.jacket@gmail.com'
    msg = "\r\n".join([
        "From: Dr. Rain <" + fromaddr + ">",
        "To: " + toaddr,
        "Subject: Rain in the Forecast! ({0}".format(probability),
        "",
        "Rain probability is {0}. You'd better bring a jacket.".format(probability)
    ])

    _server.sendmail(fromaddr, [toaddr], msg)


def close():
    _server.quit()



