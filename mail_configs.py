import ConfigParser


class MailConfigs(object):
    """
    Configurations for the mail server
    """

    def __init__(self):
        self.config = ConfigParser.RawConfigParser()
        self.config.read('dr_rain.ini')

    def username(self):
        """
        :returns string
        """
        return self.config.get('mail', 'username')

    def password(self):
        """
        :returns string
        """
        return self.config.get('mail', 'password')
