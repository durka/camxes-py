#!/usr/bin/env python

# pylint: disable=I0011,C0111

import sys

from parsimonious.exceptions import ParseError

from structures import jbovlaste_types
from camxes import configure_platform
from parsers.camxes_ilmen import Parser
from transformers.vlatai import Visitor

VLATAI_RULE = "vlatai"

def main(text):
    for word in text:
        gensuha = analyze_morphology(build_parser(), word)
        print '%s:' % word, jbovlaste_types.classify(gensuha)

def build_parser():
    return Parser(VLATAI_RULE)

def analyze_morphology(parser, text):
    visitor = Visitor()
    gensuha = None
    try:
        parsed = parser.parse(text)
        gensuha = visitor.visit(parsed)
    except ParseError:
        pass
    return gensuha

if __name__ == '__main__':
    import sys
    import itertools
    text = itertools.chain(*map(lambda s: s.split(' '), sys.argv[1:]))
    configure_platform()
    main(text)

