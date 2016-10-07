import ConfigParser
import sys

from os.path import expanduser, isfile


class PushbulletConfig(object):
    """handles reading, writing, and validating
       the configuration for pushbullet"""
    def __init__(self, configpath=None, access_token=None):
        super(PushbulletConfig, self).__init__()
        self.section = 'pushbullet'
        self.configpath = self.set_config_path(configpath)
        self.access_token = self.set_api_key(access_token)

    def set_config_path(self, configpath):
        if configpath is None:
            # set config path to the default of the users home directory
            configpath = '{0}/{1}'.format(expanduser('~'), 'pb.cfg')
        return configpath

    def set_api_key(self, access_token):
        if access_token is None:
            if isfile(self.configpath):
                access_token = self.read_config('access_token')
            else:
                print '{0} does not exist'.format(self.configpath)
                print 'create {0}, or use the -a flag'.format(self.configpath)
                sys.exit(1)
        return access_token

    def read_config(self, key):
        parser = ConfigParser.SafeConfigParser()
        parser.read(self.configpath)
        return parser.get(self.section, key)
