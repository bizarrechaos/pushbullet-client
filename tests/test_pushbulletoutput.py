import pytest

from pushbullet import pushbulletoutput


class TestPushbulletOutput(object):

    def test_device_output_with_all(self, capsys):
        d = {'devices': [{}]}
        pushbulletoutput.device_output(d, True)
        out, err = capsys.readouterr()
        fields = ['NICKNAME',
                  'IDEN',
                  'KIND',
                  'MANUFACTURER',
                  'MODEL',
                  'PUSHABLE']
        assert '{0:20} {1:30} {2:20} {3:20} {4:20} {5}'.format(*fields) in out

    def test_device_output_without_all(self):
        with pytest.raises(KeyError):
            d = {'devices': [{}]}
            pushbulletoutput.device_output(d, False)

    def test_push_output_with_unread(self, capsys):
        d = {'pushes': [{'active': True,
                         'body': 'body',
                         'created': 1,
                         'direction': 'self',
                         'dismissed': False,
                         'iden': 'ujpah72o0sjAoRtnM0jc',
                         'modified': 1,
                         'receiver_email': 'email@email.com',
                         'receiver_email_normalized': 'email@email.com',
                         'receiver_iden': 'ujpah72o0',
                         'sender_email': 'email@email.com',
                         'sender_email_normalized': 'email@email.com',
                         'sender_iden': 'ujpah72o0',
                         'sender_name': 'sender',
                         'title': 'title',
                         'type': 'note'}]}
        pushbulletoutput.push_output(d, True)
        out, err = capsys.readouterr()
        assert out == '{type:5} {iden:5} {created:5} {direction:5} '\
            '{sender_name}\n{title}\n{body}\n\n'.format(**d['pushes'][0])

    def test_push_output_without_unread(self, capsys):
        d = {'pushes': [{'active': True,
                         'body': 'body',
                         'created': 1,
                         'direction': 'self',
                         'dismissed': False,
                         'iden': 'ujpah72o0sjAoRtnM0jc',
                         'modified': 1,
                         'receiver_email': 'email@email.com',
                         'receiver_email_normalized': 'email@email.com',
                         'receiver_iden': 'ujpah72o0',
                         'sender_email': 'email@email.com',
                         'sender_email_normalized': 'email@email.com',
                         'sender_iden': 'ujpah72o0',
                         'sender_name': 'sender',
                         'title': 'title',
                         'type': 'note'}]}
        pushbulletoutput.push_output(d, False)
        out, err = capsys.readouterr()
        assert out == '{type:5} {iden:5} {created:5} {direction:5} '\
            '{sender_name}\n{title}\n{body}\n\n'.format(**d['pushes'][0])

    def test_push_output_without_unread_missing_body(self, capsys):
        d = {'pushes': [{'active': True,
                         'created': 1,
                         'direction': 'self',
                         'dismissed': False,
                         'iden': 'ujpah72o0sjAoRtnM0jc',
                         'modified': 1,
                         'receiver_email': 'email@email.com',
                         'receiver_email_normalized': 'email@email.com',
                         'receiver_iden': 'ujpah72o0',
                         'sender_email': 'email@email.com',
                         'sender_email_normalized': 'email@email.com',
                         'sender_iden': 'ujpah72o0',
                         'sender_name': 'sender',
                         'title': 'title',
                         'type': 'note'}]}
        pushbulletoutput.push_output(d, False)
        out, err = capsys.readouterr()
        assert out == '{type:5} {iden:5} {created:5} {direction:5} '\
            '{sender_name}\n{title}\nNone\n\n'.format(**d['pushes'][0])

    def test_pushed_output_success(self, capsys):
        pushbulletoutput.pushed_output({'test': 'test'})
        out, err = capsys.readouterr()
        assert out == 'push sent\n'

    def test_pushed_output_fail(self, capsys):
        pushbulletoutput.pushed_output(None)
        out, err = capsys.readouterr()
        assert out == 'push failed\n'
