import json
import pytest
import responses

from pushbullet import pushbulletapi


class TestPushbulletAPI(object):

    def test_pushbullet_api(self):
        p = pushbulletapi.PushbulletAPI('testapikey')
        assert p.access_token == 'testapikey'
        assert p.baseurl == 'https://api.pushbullet.com/v2'
        assert p.deviceuri == '/devices'
        assert p.pushuri == '/pushes'

    @responses.activate
    def test_get_devices(self):
        p = pushbulletapi.PushbulletAPI('testapikey')
        responses.add(responses.GET,
                      '{0}{1}'.format(p.baseurl, p.deviceuri),
                      status=200,
                      body=json.dumps({}))
        assert p.get_devices() == {}

    @responses.activate
    def test_get_device_by_name(self):
        p = pushbulletapi.PushbulletAPI('testapikey')
        responses.add(responses.GET,
                      '{0}{1}'.format(p.baseurl, p.deviceuri),
                      status=200,
                      body=json.dumps({'devices': [{'nickname': 'test',
                                                    'iden': 'test'}]}))
        assert p.get_device_by_name('test') == 'test'

    @responses.activate
    def test_get_pushes(self):
        p = pushbulletapi.PushbulletAPI('testapikey')
        responses.add(responses.GET,
                      '{0}{1}'.format(p.baseurl, p.pushuri),
                      status=200,
                      body=json.dumps({}))
        assert p.get_pushes() == {}

    @responses.activate
    def test_push(self):
        p = pushbulletapi.PushbulletAPI('testapikey')
        responses.add(responses.POST,
                      '{0}{1}'.format(p.baseurl, p.pushuri),
                      status=200,
                      body=json.dumps({}))
        assert p.push('test', 'test', 'test', target='test', url='test') == {}
