import ConfigParser


class WeatherConfigs(object):
    """
    Configurations for the mail server
    """

    def __init__(self):
        self.config = ConfigParser.RawConfigParser()
        self.config.read('dr_rain.ini')

    def api_key(self):
        """
        :returns string
        """
        return self.config.get('weather', 'api_key')
