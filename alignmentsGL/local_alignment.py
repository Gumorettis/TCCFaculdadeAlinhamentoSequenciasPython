from alignment import Alignment

class LocalAlignment(Alignment):

    type = 'Local Alignment'

    def run(self):

        m = len(self.s) + 1
        n = len(self.t) + 1

        self.a = [
            [0 for j in range(n)] for i in range(m)
        ]

        for i in range(1, m):

            for j in range(1, n):
                value = self.score.match if self.s[i - 1] == self.t[j - 1] else self.score.mismatch
                self.a[i][j] = max(
                    self.a[i - 1][j] + self.score.gap,
                    self.a[i - 1][j - 1] + value,
                    self.a[i][j - 1] + self.score.gap,
                    0
                )

                if self.a[i][j] > self.similarity:
                    self.similarity = self.a[i][j]
                    self.similarity_positions = [[i, j]]

                elif self.a[i][j] == self.similarity:
                    self.similarity_positions.append([i, j])

        self.similarity_positions = [self.similarity_positions[0]]

    def __calc_alignment(self, i, j, s, t): #calcula o traceback de forma recursiva
        if self.a[i][j] == 0:
            self.alignments = [
                t[::-1], s[::-1]
            ]

            return

        if i > 0 and j > 0 and self.a[i][j] == self.a[i - 1][j - 1] + (
                self.score.match if self.s[i - 1] == self.t[j - 1] else self.score.mismatch
        ):
            self.__calc_alignment(
                i=i - 1,
                j=j - 1,
                s=s + self.s[i - 1],
                t=t + self.t[j - 1]
            )

        elif i > 0 and self.a[i][j] == self.a[i - 1][j] + self.score.gap:
            self.__calc_alignment(
                i=i - 1,
                j=j,
                s=s + self.s[i - 1],
                t=t + '_'
            )

        elif j > 0 and self.a[i][j] == self.a[i][j - 1] + self.score.gap:
            self.__calc_alignment(
                i=i,
                j=j - 1,
                s=s + '_',
                t=t + self.t[j - 1]
            )

    def __calc_alignment_iterativo(self, i, j, s, t):

        while self.a[i][j] != 0:
            if i > 0 and j > 0 and self.a[i][j] == self.a[i - 1][j - 1] + (self.score.match if self.s[i - 1] == self.t[j - 1] else self.score.mismatch):  # diagonal superior
                s += self.s[i - 1]
                t += self.t[j - 1]
                i -= 1
                j -= 1

            elif i > 0 and self.a[i][j] == self.a[i - 1][j] + self.score.gap:  # cima
                s += self.s[i - 1]
                i -= 1
                t += '_'

            elif j > 0 and self.a[i][j] == self.a[i][j - 1] + self.score.gap:  # esquerda
                s += '_'
                t += self.t[j - 1]
                j -= 1

        self.alignments = [
            t[::-1], s[::-1]
        ]

    def get_alignments(self):

        self.alignments = []

        for [i, j] in self.similarity_positions:
            self.__calc_alignment_iterativo(
                i=i,
                j=j,
                s='',
                t=''
            )

        return self.alignments