#!/bin/python3

# I am not 100% convinced that python is the best language for this. However, it's extremely easy to use. I might switch to some other language in the future.

import os
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Simple website generator')
    parser.add_argument('markdown', metavar='MD', type=str, help='The markdown file to parse')
    parser.add_argument('-o', '--output', help='The file to output the html file to')

    args = parser.parse_args()

    if not os.path.exists(args.markdown):
        raise FileNotFoundError('File {} not found'.format(args.markdown))
        sys.exit(1)
    if os.path.exists(args.output):
        print('{} already exists. Overwritting...'.format(args.output))

    return args

def run():
    args = parse_args()
    cmd = ''
    if args.output == None:
        cmd = 'markdown {} -o index1.html'.format(args.markdown)
    else:
        cmd = 'markdown -o {} {}'.format(args.output, args.markdown)
    os.system(cmd)

if __name__ == '__main__':
    run()
