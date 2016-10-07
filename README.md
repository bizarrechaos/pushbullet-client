#pushbullet-client [![Build Status](https://travis-ci.org/bizarrechaos/pushbullet-client.svg?branch=master)](https://travis-ci.org/bizarrechaos/pushbullet-client)

Python libraries and command line interface for Pushbullet

####Installation:

You can install the latest available version of pushbullet-client from GitHub using pip:

```
pip install git+git://github.com/bizarrechaos/pushbullet-client.git
```

You can also clone the repository and install pushbullet-client:

```
git clone https://github.com/bizarrechaos/pushbullet-client.git
cd pushbullet-client
python setup.py install
```

####Usage overview:
```
Usage:
    pushbullet device list [all] [options]
    pushbullet push list [unread] [options]
    pushbullet push note [id <iden>|name <name>] <title> <body> [options]
    pushbullet push link [id <iden>|name <name>] <title> <body> <url> [options]

Options:
    -a <token>, --access-token <token>      Provide an access token.
    -h, --help                              Show this page.
    -v, --version                           Show the application version
```

######powered by [pushbullet](https://www.pushbullet.com/)
