"""pushbullet

Usage:
    pushbullet device list [all] [options]
    pushbullet push list [unread] [options]
    pushbullet push note [id <iden>|name <name>] <title> <body> [options]
    pushbullet push link [id <iden>|name <name>] <title> <body> <url> [options]

Options:
    -a <token>, --access-token <token>      Provide an access token.
    -h, --help                              Show this page.
    -v, --version                           Show the application version.
"""

from docopt import docopt

from . import pushbulletapi
from . import pushbulletconfig
from . import pushbulletoutput


def main():
    args = docopt(__doc__, version='pushbullet.py 1.0')
    pc = pushbulletconfig.PushbulletConfig(access_token=args['--access-token'])
    pb = pushbulletapi.PushbulletAPI(pc.access_token)
    if args['device']:
        if args['list']:
            pushbulletoutput.device_output(pb.get_devices(), args['all'])
    elif args['push']:
        if args['list']:
            pushbulletoutput.push_output(pb.get_pushes(), args['unread'])
        elif args['note'] or args['link']:
            if args['name'] or args['id']:
                if args['name']:
                    args['<iden>'] = pb.get_device_by_name(args['<name>'])
                if args['note']:
                    push = pb.push('note', args['<title>'], args['<body>'],
                                   target=args['<iden>'])
                elif args['link']:
                    push = pb.push('link', args['<title>'], args['<body>'],
                                   target=args['<iden>'], url=args['<url>'])
            else:
                if args['note']:
                    push = pb.push('note', args['<title>'], args['<body>'])
                elif args['link']:
                    push = pb.push('link', args['<title>'],
                                   args['<body>'], url=args['<url>'])
            pushbulletoutput.pushed_output(push)


if __name__ == "__main__":
    main()
