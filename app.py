#!/bin/python3

# I am not 100% convinced that python is the best language for this. However, it's extremely easy to use. I might switch to some other language in the future.

import os
import subprocess
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Simple website generator')
    parser.add_argument('markdown', metavar='MD', type=str, help='The markdown file to parse')
    parser.add_argument('-o', '--output', help='Name of the webpage')

    args = parser.parse_args()

    if not os.path.exists(args.markdown):
        raise FileNotFoundError('File {} not found'.format(args.markdown))
        sys.exit(1)
    if args.output == None:
        return args
    if os.path.exists(args.output + '.html'):
        print('{} already exists. Overwritting...'.format(args.output))

    return args

def make_html(markdown, output):
    p = subprocess.Popen(['markdown', markdown], shell=False, stdout=subprocess.PIPE)
    op = p.stdout.read().decode()

    final_op = ''
    with open('./static/template.html', 'r') as html:
        data = html.read()
        final_op = data.format(output.capitalize(), op)
    with open(output + '.html', 'w') as f:
        f.write(final_op)

def run():
    args = parse_args()
    output = args.output if args.output != None else 'Website'
    make_html(args.markdown, output)

if __name__ == '__main__':
    run()
