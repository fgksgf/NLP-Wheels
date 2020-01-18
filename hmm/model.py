class HMM:
    def __init__(self, A, B, PI):
        self.A = A
        self.B = B
        self.PI = PI

    def evaluation(self, O):
        pass

    def __forward_procedure(self):
        pass

    def __backward_procedure(self):
        pass

    def __viterbi_algorithm(self):
        delta = {}
        psi = {}
        pass

    def decoding(self, O):
        pass

    def parameter_learning(self):
        pass


if __name__ == '__main__':
    states = ['高兴', '平静', '生气']
    objects = ['嗯嗯', '好的']
    A = [
        [0.6, 0.3, 0.1],
        [0.4, 0.5, 0.1],
        [0.3, 0.4, 0.3]
    ]

    B = [
        [0.4, 0.6],
        [0.5, 0.5],
        [0.8, 0.2]
    ]

    PI = [0.4, 0.5, 0.1]
    mu = HMM(A, B, PI)
