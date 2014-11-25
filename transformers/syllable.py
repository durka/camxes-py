from parsimonious.nodes import NodeVisitor
from compiler.ast import flatten
from transformers import find_all

class Transformer:

  def __init__(self, trim):
    self.trim = trim

  def transform(self, parsed):
    return Visitor(self.trim).visit(parsed)

class Visitor(NodeVisitor):

  def __init__(self, trim):
    self.trim = trim

  def visit_jbocme(self, node, visited_children):
    kids = filter(lambda x: len(x) > 0, flatten(visited_children))
    if not any(map(lambda k: any(map(lambda c: c.isupper(), k)), kids)):
      vocalic_kids = filter(lambda k: 'y' not in k[1]
                                      and any(map(lambda v: v in k[1],
                                                  'aeiou')),
                            zip(range(len(kids)), kids))
      if len(vocalic_kids) > 1:
        i = vocalic_kids[-2][0]
        kids[i] = kids[i].upper()
    return ','.join(kids)

  def visit_zifcme(self, node, visited_children):
    return node.text

  def visit_cmevla(self, node, visited_children):
    return visited_children[0]

  def visit_any_syllable(self, node, visited_children):
    if any(map(lambda c: c.isupper(), node.text)):
      text = node.text.upper()
    else:
      text = node.text

    if self.trim < 0 and node.end == len(node.full_text):
      return text[:self.trim]
    if self.trim > 0 and node.start < self.trim:
      return text[(self.trim-node.start):]
    return text

  def generic_visit(self, node, visited_children):
    return flatten(visited_children)


