#!/usr/bin/env python

import os
import json

from camxes import VERSION, configure_platform
from parsers import camxes_ilmen
from transformers import node_coverage

TEST_DIRECTORY  = "test"
INPUT_FILENAME  = "camxes_ilmen_js.json"

PWD = os.path.dirname(__file__)
INPUT_PATH = os.path.join(PWD, TEST_DIRECTORY, INPUT_FILENAME)

def main():
  input_json = read_json(INPUT_PATH)
  visits = process_input(input_json)
  print json.dumps(visits, indent=4)

def read_json(path):
  input_file = open(path)
  input_json = json.load(input_file)
  input_file.close()
  return input_json

def process_input(input_json):
  input_specs = input_json["specs"]
  parser = camxes_ilmen.Parser()
  transformer = node_coverage.Transformer(parser)
  for spec in input_specs:
    if spec["out"] != "ERROR":
      parsed = parser.parse(spec["txt"])
      transformer.visit(parsed)
  return transformer.visits()

if __name__ == '__main__':
  configure_platform()
  main()

