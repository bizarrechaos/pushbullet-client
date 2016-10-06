"""pushbullet
"""

from docopt import docopt

from . import pushbulletapi


def main():
    args = docopt(__doc__, version='pushbullet.py 1.0')
    pushbulletapi.Pushbullet(args)

if __name__ == "__main__":
    main()
