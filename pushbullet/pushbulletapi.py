import json
import requests


from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class PushbulletAPI(object):
    """docstring for PushbulletAPI."""
    def __init__(self, access_token):
        super(PushbulletAPI, self).__init__()
        self.access_token = access_token
        self.headers = {'Access-Token': self.access_token,
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'}
        self.baseurl = 'https://api.pushbullet.com/v2'
        self.deviceuri = '/devices'
        self.pushuri = '/pushes'

    def get_devices(self):
        r = requests.get('{0}{1}'.format(self.baseurl, self.deviceuri),
                         headers=self.headers)
        if r.ok:
            return r.json()

    def get_device_by_name(self, name):
        for d in self.get_devices()['devices']:
            if 'nickname' in d:
                if d['nickname'].lower() == name.lower():
                    return d['iden']

    def get_pushes(self):
        r = requests.get('{0}{1}'.format(self.baseurl, self.pushuri),
                         headers=self.headers)
        if r.ok:
            return r.json()

    def push(self, type, title, body, target=None, url=None):
        data = {'body': body, 'title': title, 'type': 'note'}
        if url is not None:
            data['url'] = url
        if target is not None:
            data['device_iden'] = target
        r = requests.post('{0}{1}'.format(self.baseurl, self.pushuri),
                          headers=self.headers, data=json.dumps(data))
        if r.ok:
            return r.json()
