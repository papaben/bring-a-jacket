"""
Send emails from Dr. Rain
"""
import logging
from mail_server import MailServer
from dr_rain_configs import DrRainConfigs


# A little gunny sack to memoize the mail server
_memorandum = {
    '_initialized': False,
    '_server': None,
}

_logger = logging.getLogger(__name__)


def it_gunna_rain(probability, to_addr):
    """
    Send an email about the rain
    :param probability: string
    :param to_addr: string
    """
    subject = "Rain in the Forecast! ({0})".format(probability)
    body = "Rain probability is {0}. You'd better bring a jacket.".format(probability)

    _logger.debug("Sending email to {0}".format(to_addr))
    _get_server().send(to_addr, subject, body)


def close():
    """
    Close active connection to mail server
    """
    if _memorandum['_initialized']:
        _logger.info("Closing connection to mail server")
        _get_server().quit()


def _get_server():
    """
    :returns MailServer
    """
    if not _memorandum['_initialized']:
        configs = DrRainConfigs()
        _logger.info("Initializing connection to mail server")
        # Reduce open connections by sharing a single server object
        server = MailServer(configs.mail_username(), configs.mail_password())

        _memorandum['_server'] = server
        _memorandum['_initialized'] = True

    return _memorandum['_server']


if __name__ == "__main__":
    print "Please see README"
