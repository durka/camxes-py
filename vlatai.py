#!/usr/bin/env python

# pylint: disable=I0011,C0111

import sys

from parsimonious.exceptions import ParseError

from structures import jbovlaste_types
from camxes import configure_platform
from parsers.camxes_ilmen import Parser
from transformers.vlatai import Visitor

VLATAI_RULE = "vlatai"

def main(text, simple):
    for word in text:
        gensuha = analyze_morphology(build_parser(), word)
        velski = jbovlaste_types.classify(gensuha, simple)
        if simple:
            print velski
        else:
            print '%s:' % word, velski

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
    import itertools

    from optparse import OptionParser
    from camxes import VERSION
    usage_fmt = "usage: %prog [ options ] { input }"
    options = OptionParser(usage=usage_fmt, version="%prog " + VERSION)
    options.add_option("-s", "--simple",
                                         help="enable simple output (for jbovlaste)",
                                         action="store_true",
                                         dest="simple")
    (params, argv) = options.parse_args()

    text = itertools.chain(*map(lambda s: s.split(' '), argv))
    configure_platform()
    main(text, params.simple)

