#!/usr/bin/env python
"""A lightweight script to compile static websites with jinja2 and structured data"""

import sys
import argparse
import jinja2
import ujson as json
import cPickle as pickle


def get_params():
    parser = argparse.ArgumentParser(description='Static compilation of jinja templates')

    parser.add_argument(    'input_template',
                            action      =   'store',
                            help        =   'path to the input template file')

    parser.add_argument(    '-d',
                            '--data',
                            dest        =   'data',
                            required    =   False,
                            type        =   str,
                            help        =   'path to the input data file (json or pickle)')

    parser.add_argument(    '-o',
                            '--output',
                            dest        =   'output_path',
                            required    =   False,
                            type        =   str,
                            help        =   'path to save the rendered template')

    return vars(parser.parse_args(sys.argv[1:]))

def main():
    args = get_params()
    print args

if __name__ == '__main__':
    main()

