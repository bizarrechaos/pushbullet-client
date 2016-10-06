from setuptools import setup


setup(
    name='pushbullet-client',
    version='1.0',
    author='bizarrechaos',
    packages=['pushbullet'],
    license='Apache License Version 2.0',
    description='Python libraries and command line interface for Pushbullet',
    install_requires=['docopt==0.6.2',
                      'requests==2.11.1'],
    url='https://github.com/bizarrechaos/pushbullet-client',
    entry_points='''
        [console_scripts]
        pushbullet = pushbullet.__main__:main
    '''
)
