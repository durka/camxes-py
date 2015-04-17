
# pylint: disable=I0011, C0111, C0326

from structures.gensuha \
  import Cmevla, Gismu, Lujvo, Fuhivla, Fuhivla3, Fuhivla35, Fuhivla4, \
         Cmavo, ZeiLujvo, BuLetteral, Tosmabru, Slinkuhi

# legacy classifications
CMEVLA        = "cmevla"
GISMU         = "gismu"
LUJVO         = "lujvo"
FUHIVLA       = "fu'ivla"
CMAVO         = "cmavo"
NALVLA        = "nalvla"

# new classifications
CMAVO_COMPOUND = "cmavo-compound"
BU_LETTERAL    = "bu-letteral"
ZEI_LUJVO      = "zei-lujvo"

# non-jvs types
TOSMABRU       = "valrtosmabru"
SLINKUHI       = "valslinku'i"

def classify(gensuha, simple=False):
    if gensuha is None or len(gensuha) < 1:
        return NALVLA
    elif len(gensuha) == 1:
        return classify_gensuha(gensuha[0], simple)
    else:
        return classify_gensuha_sequence(gensuha, simple)

def classify_gensuha(gensuha, simple=False):
  if isinstance(gensuha, Cmevla):
    return CMEVLA
  elif isinstance(gensuha, Gismu):
    return GISMU
  elif isinstance(gensuha, Lujvo):
    if simple:
      return LUJVO
    return '%s/%s' % (LUJVO, '-'.join(gensuha.rafsi))
  elif isinstance(gensuha, Fuhivla):
    if simple:
      return FUHIVLA
    if isinstance(gensuha, Fuhivla3):
      return '%s/%s/%s-%s' % (FUHIVLA, gensuha.type, gensuha.rafsi, gensuha.payload)
    return '%s/%s' % (FUHIVLA, gensuha.type)
  elif isinstance(gensuha, Cmavo):
    if simple:
      return CMAVO
    return '%s/%s' % (CMAVO, gensuha.selmaho)
  elif isinstance(gensuha, ZeiLujvo):
    return ZEI_LUJVO
  elif isinstance(gensuha, BuLetteral):
    return BU_LETTERAL
  elif isinstance(gensuha, Tosmabru):
    if simple:
      return TOSMABRU
    return '%s (%s)' % (TOSMABRU, classify_gensuha_sequence(gensuha.vlapoi))
  elif isinstance(gensuha, Slinkuhi):
    return SLINKUHI
  else:
    return NALVLA

def classify_gensuha_sequence(gensuha, simple=False):
  if simple:
    if is_cmavo_sequence(gensuha):
      return CMAVO_COMPOUND
    else:
      return NALVLA
  else:
    return ' '.join(map(lambda g: '%s=%s' % (''.join(g.lerpoi), classify_gensuha(g, simple)), gensuha))

def is_cmavo_sequence(gensuha):
    return all(isinstance(g, Cmavo) for g in gensuha)

