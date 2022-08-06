#Classe responsavel pelo score do alinhamento
class Score(object):
    def __init__(self, match, mismatch, gap):
        self.match = match
        self.mismatch = mismatch
        self.gap = gap
