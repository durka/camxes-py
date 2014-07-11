from parsimonious import grammar as pg
from collections import OrderedDict

class Visitor(pg.RuleVisitor):
    def visit_rules(self, node, visited_children):
        return pg.RuleVisitor.visit_rules(self, node, visited_children)[0]


pg.Literal._as_rhs    = lambda self: u'"%s"' % self.literal if len(self.literal) > 0 else u'()'
pg.Regex._as_rhs      = lambda self: u'?/%s/?' % self.re.pattern # does not support flags
pg.Sequence._as_rhs   = lambda self: u'( %s )' % u' '.join(self._unicode_members())
pg.OneOf._as_rhs      = lambda self: u'( %s )' % u' | '.join(self._unicode_members())
pg.Optional._as_rhs   = lambda self: u'[ %s ]' % self._unicode_members()[0]
pg.ZeroOrMore._as_rhs = lambda self: u'{ %s }*' % self._unicode_members()[0]
pg.OneOrMore._as_rhs  = lambda self: u'{ %s }+' % self._unicode_members()[0]

def visit_rules(self, node, (_, rules)):
    """Collate all the rules into a map. Return (map, default rule).

The default rule is the first one. Or, if you have more than one rule
of that name, it's the last-occurring rule of that name. (This lets you
override the default rule when you extend a grammar.)

"""
    # Map each rule's name to its Expression. Later rules of the same name
    # override earlier ones. This lets us define rules multiple times and
    # have the last declarations win, so you can extend grammars by
    # concatenation.
    rule_map = OrderedDict((expr.name, expr) for expr in rules)

    # Resolve references. This tolerates forward references.
    unwalked_names = set(rule_map.iterkeys())
    while unwalked_names:
        rule_name = next(iter(unwalked_names)) # any arbitrary item
        rule_map[rule_name] = self._resolve_refs(rule_map,
                                                 rule_map[rule_name],
                                                 unwalked_names,
                                                 (rule_name,))
        unwalked_names.discard(rule_name)
    return rule_map, rules[0]
pg.RuleVisitor.visit_rules = visit_rules




with open('parsers/camxes_ilmen.peg', 'r') as f:
    peg = Visitor().visit(pg.Grammar(pg.rule_syntax).parse(f.read()))

with open('parsers/camxes_ilmen.gpeg', 'w') as f:
    for rule, sequence in peg.iteritems():
        print >>f, '%s = %s:( %s ) ;' % (rule, rule, sequence._as_rhs())

