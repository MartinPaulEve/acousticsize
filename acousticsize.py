"""Music release generator.

Usage:
  acousticsize.py <height>
  acousticsize.py (-h | --help)
  acousticsize.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.

Info:

Calculates Bolt-ratio room sizes based on a height input

"""
import os
from docopt import docopt
import logging
import pygogo as gogo
from formatter import Formatter


ratios = [
    {'name': 'Sepmeyer B',
     'width': 1.28,
     'length': 1.54},
    {'name': 'Sepmeyer C',
     'width': 1.6,
     'length': 2.33},
    {'name': 'Louden D',
     'width': 1.4,
     'length': 1.9},
    {'name': 'Louden F',
     'width': 1.5,
     'length': 2.5},
    {'name': 'Volkmann',
     'width': 1.5,
     'length': 2.5},
    {'name': 'Boner',
     'width': 1.26,
     'length': 1.59}
]

app = "Acoustic Size Calculator 1.0"

log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(log_format)

logger = gogo.Gogo(
    'ASC',
    low_formatter=formatter,
    high_formatter=formatter,
    monolog=True).logger


def main(args):
    logger.setLevel('INFO')

    if '<height>' in args:
        for ratio in ratios:
            output = "\n" + Formatter.format_line('Height', args['<height>']) + "\n"
            output += Formatter.format_line('Width', float(args['<height>']) * ratio['width']) + "\n"
            output += Formatter.format_line('Length', float(args['<height>']) * ratio['length']) + "\n"
            Formatter.print_res(ratio['name'], output)


if __name__ == "__main__":
    arguments = docopt(__doc__, version=app)
    main(arguments)