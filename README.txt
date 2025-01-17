
camxes-py is a pure Python implementation of the lojban "camxes" PEG parser.
From v0.6, camxes-py uses updated, v119 camxes morphology. Earlier versions
used v108 morphology.

USAGE
=====

By default, input is parsed and transformed to the output format used by the
ilmentufa implementation of camxes.js:

    python camxes.py "coi munje"

To parse potentially non-grammatical texts into cmevla, brivla, cmavo and
non-lojban words, specify the "camxes-morphology" transformation and the
"morphology" starting expression:

    python camxes.py -t camxes-morphology "coi munje"

To parse using jbovlaste's categories, which add bu-letteral, zei-lujvo, and
cmavo-compound to the standard morphological ones, use the "vlatai" rule
transformation:

    python camxes.py -t vlatai -r vlatai "coi zei munje bu"

OPTIONS
=======

The --transformer (-t) option controls the transformation of the parse tree.
Supported options include: raw, debug, node-coverage, camxes-morphology, vlatai,
and camxes-json (default)

The --serializer (-s) option controls the serialization of the transformed
parse tree. Supported options include: json, json-pretty, and
json-compact (default)

The --rule (-r) option is used to specify the starting rule or expression used
to parsed the text. By default, the first rule of the grammar ("text") is used.

DEPENDENCIES
============

camxes-py depends on the "parsimonious" PEG parser library, and has been
tested under CPython 2.7.4 and PyPy 2.2.1. To run the IRC bot, the "twisted"
library is also required.

TESTING
=======

camxes-py is tested with the corpus of more than 22K test sentences
that Robin Lee Powell originally assembled to test the first (Java Rats!)
camxes implementation.

These sentences have been converted to UTF-8, indexed by MD5/base64 token,
deduplicated and packaged in "sentences.json" in the "test" directory.
Each sentence is marked "GOOD" or "BAD" if it was so-commented in the
original source file; other sentences are marked "UNKNOWN".

Running "test.py" will parse all of the test sentences, comparing the results
to the output of ilmentufa camxes.js (cached in "camxes_ilmen_js.json")
and regenerating "camxes_ilmen_py.json". Running "cover.py" will produce
a json-formatted list of the nodes produced by parsing the test corpus,
ordered by descending frequency and expression name.

LICENSE
=======

The scripts and modules in this implementation may be copied, modified,
and distributed under the terms of the accompanied license, "LICENSE.txt".

ACKNOWLEDGMENTS
===============

camxes-py draws on prior implementations of the "camxes" PEG parser, including
the original Java Rats! implementation by Robin Lee Powell and Jorge Llambías,
the JavaScript port (camxes.js) by Masato Hagiwara. It owes an immediate debt
to the "ilmentufa" parser by Ilmen, which corrected camxes' handling of sumti
tcita and extended camxes.js with suppport for ZOI quotations and elided
terminator detection.

The camxes-py IRC bot is based loosely on the "valsi" and "gerna" bots written
by Dag Odenhall for "vlasisku".

