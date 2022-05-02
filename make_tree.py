#!/usr/bin/env python

from itertools import groupby
import argparse
import json


# Replacement for accentuated characters
REPLACEMENT = {
    'é': 'e',
    'ê': 'e',
    'è': 'e',
    'ö': 'o',
    'ô': 'o',
    'ä': 'a',
    'à': 'a',
    'â': 'a',
    'î': 'i',
    'ï': 'i',
    'û': 'u',
    'ù': 'u',
    'ç': 'c',
}


def remove_accents(mot):
    res = ''
    for lettre in mot:
        if lettre in REPLACEMENT:
            res += REPLACEMENT[lettre]
        else:
            res += lettre
    return res


def get_parser():
    parser = argparse.ArgumentParser(
        description='Generates a tree from a list of words'
    )
    parser.add_argument(
        'input_file',
        help='a text file containing a list of words. One word per line'
    )
    parser.add_argument(
        '-m',
        '--min-length',
        type=int, default=2,
        help='the minimum length allowed. Shorter words will be discarded'
    )
    parser.add_argument(
        '-M',
        '--max-length',
        type=int,
        default=7,
        help='the maximum length allowed. Longer words will be discarded'
    )

    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()

    with open(args.input_file) as f:
        MOTS = []
        for mot in f.readlines():
            mot = remove_accents(mot[:-1])
            mot = mot.upper()

            if len(mot) <= args.max_length and len(mot) >= args.min_length:
                MOTS.append(mot + '.')

    # Creating dictionary
    dico = {}

    for i in range(1, args.max_length + 1):

        for k, g in groupby(MOTS, lambda m: m[:i]):
            if k[-1] == '.':
                continue

            dico[k] = set()

            for mot in list(g):
                if mot[i] == '.':
                    dico[k].add('.')
                else:
                    dico[k].add(mot[:i+1])
            dico[k] = list(dico[k])

    print(json.dumps(dico, indent=4))


if __name__ == '__main__':
    main()
