"""
Send emails from Dr. Rain
"""
from mail_server import MailServer


_username = 'bring.a.jacket@gmail.com'

# A little gunny sack to memoize the mail server
_memorandum = {
    '_initialized': False,
    '_server': None,
}


def send_it_will_rain_email(probability, to_addr):
    """
    Send an email about the rain
    :param probability: string
    :param to_addr: string
    """
    subject = "Rain in the Forecast! ({0})".format(probability),
    body = "Rain probability is {0}. You'd better bring a jacket.".format(probability)

    _get_server().send(to_addr, subject, body)


def close():
    """
    Close active connection to mail server
    """
    if _memorandum['_initialized']:
        _get_server().quit()


def _get_server():
    """
    :returns MailServer
    """
    if not _memorandum['_initialized']:
        # Reduce open connections by sharing a single server object
        server = MailServer(_username, 'DrKnock#rs')

        _memorandum['_server'] = server
        _memorandum['_initialized'] = True

    return _memorandum['_server']


