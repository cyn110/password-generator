"""
Generate random passwords

Usage:
    PasswordGenerator.py [-h -l -c -C -d -s]
Options:
    -h, --help        <-- you are here
    -l, --length      number of the characters (default: 16)
    -c, --lower       exclude lowercase (off)
    -C, --upper       exclude uppercase (off)
    -d, --digit       exclude digit (off)
    -s, --symbol      exclude symbol (off)
"""

import sys
import getopt
import random

length = 16
use_lower = True
use_upper = True
use_symbol = True
use_digit = True

LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SYMBOL = ' !"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'
DIGIT = '1234567890'


def main():
    check_args()
    generate_password()


def usage():
    print(__doc__)


def check_args():
    global length, use_lower, use_upper, use_symbol, use_digit
    try:
        opts, args = getopt.getopt(sys.argv[1:],
                                   'hl:cCds',
                                   ['help=', 'length=', 'lower=', 'upper=', 'digit=', 'symbol='])
    except getopt.GetoptError:
        usage()
        exit(2)
    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
            exit()
        elif o in ('-l', '--length'):
            if length < 1:
                print('length can not be 0.')
                exit(1)
            else:
                length = int(a)
        elif o in ('-c', '--lower'):
            use_lower = False
        elif o in ('-C', '--upper'):
            use_upper = False
        elif o in ('-d', '--digit'):
            use_digit = False
        elif o in ('-s', '--symbol'):
            use_symbol = False

    if not (use_lower or use_upper or use_symbol or use_digit):
        print('-l, -c, -C, -d, -s cannot be used all at once')
        exit(1)


def generate_password():
    global length, use_lower, use_upper, use_symbol, use_digit
    r = random.SystemRandom()

    char_set = ''
    if use_lower:
        char_set += LOWERCASE
    if use_upper:
        char_set += UPPERCASE
    if use_symbol:
        char_set += SYMBOL
    if use_digit:
        char_set += DIGIT

    password = ''
    for i in range(1, length + 1):
        password += r.choice(char_set)

    print(password)


if __name__ == '__main__':
    main()
