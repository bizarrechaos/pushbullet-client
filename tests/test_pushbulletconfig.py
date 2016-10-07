import pytest

from pushbullet import pushbulletconfig


class TestPushbulletConfig(object):

    def test_pushbullet_config_with_path(self):
        p = pushbulletconfig.PushbulletConfig('./pb.cfg.example')
        assert p.configpath == './pb.cfg.example'

    def test_pushbullet_config_without_path(self, capsys):
        try:
            with pytest.raises(SystemExit):
                p = pushbulletconfig.PushbulletConfig()
        except:
            p = pushbulletconfig.PushbulletConfig()
            assert p.access_token == p.set_api_key(None)

    def test_pushbullet_config_with_tmp_path(self):
        with pytest.raises(SystemExit):
            p = pushbulletconfig.PushbulletConfig('/tmp/notafile')
