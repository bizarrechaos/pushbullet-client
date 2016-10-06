import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Pushbullet(object):
    """docstring for Pushbullet."""
    def __init__(self, arg):
        super(Pushbullet, self).__init__()
        self.arg = arg
