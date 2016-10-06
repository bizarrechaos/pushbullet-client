import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class PushbulletAPI(object):
    """docstring for PushbulletAPI."""
    def __init__(self, arg):
        super(PushbulletAPI, self).__init__()
        self.arg = arg
