import ConfigParser


class DrRainConfigs(object):
    """
    Configurations for the mail server
    """

    def __init__(self):
        self.config = ConfigParser.RawConfigParser()
        self.config.read('dr_rain.ini')

    @staticmethod
    def print_readme():
        return """
        General configurations for the Dr. Rain application.

        [mail]
        username = dr-rain
        password = dr-rain-password

        [weather]
        api_key = <<api key for weather.io>>
        """

    def mail_username(self):
        """
        :returns string
        """
        return self.config.get('mail', 'username')

    def mail_password(self):
        """
        :returns string
        """
        return self.config.get('mail', 'password')

    def weather_api_key(self):
        """
        :returns string
        """
        return self.config.get('weather', 'api_key')
