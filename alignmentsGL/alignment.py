import sys

class Alignment(object):
    type = ''

    def __init__(self, s, t, score):
        if len(s) >= len(t):
            self.t = s
            self.s = t
        else:
            self.t = t
            self.s = s
        self.score = score
        self.a = []
        self.alignments = []
        self.similarity = -sys.maxsize
        self.similarity_positions = []

    def get_matrix(self):
        return self.a

    def get_similarity(self):
        return self.similarity

    def run(self):
        raise NotImplementedError('Method "run" is not implemented yet.')

    def __calc_alignment(self, i, j, s, t):
        raise NotImplementedError('Method "__calc_alignment" is not implemented yet.')

    def get_alignments(self):
        raise NotImplementedError('Method "get_alignments" is not implemented yet.')

    def __str__(self):
        matrix = 'Matrix\n' + '\n'.join([''.join(['{:6}'.format(item) for item in row]) for row in self.a])
        similarity = 'Similarity: {0}\n'.format(self.similarity)
        alignments = 'Result Sequences: \n\n' + '\n'.join(
            'T: {0}\nS: {1}\n'.format(t, s) for [t, s] in self.get_alignments()
        )

        return '== {type} ==\n\n{matrix}\n\n{similarity}\n{alignments}'.format(
            type=self.type,
            matrix=matrix,
            similarity=similarity,
            alignments=alignments
        )
