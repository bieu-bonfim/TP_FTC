from State import *


class Jokenpo_AFD:
    def __init__(self) -> None:
        q0 = State(0, {0: 1, 1: 2, 2: 3})

        q1 = State(1, {0: 5, 1: 4, 2: 6})
        q2 = State(2, {0: 6, 1: 5, 2: 4})
        q3 = State(3, {0: 4, 1: 6, 2: 5})

        q4 = State(4, {0: 22, 1: 23, 2: 24})
        q5 = State(5, {0: 7, 1: 8, 2: 9})
        q6 = State(6, {0: 19, 1: 20, 2: 21})

        q7 = State(7, {0: 11, 1: 12, 2: 10})
        q8 = State(8, {0: 10, 1: 11, 2: 12})
        q9 = State(9, {0: 12, 1: 10, 2: 11})

        q10 = State(10, {0: 18, 1: 25, 2: 26})
        q11 = State(11, {0: 32, 1: 33, 2: 34})
        q12 = State(12, {0: 27, 1: 28, 2: 29})

        q13 = State(13, {0: 17, 1: 17, 2: 17})

        q14 = State(14, {0: "Erro", 1: "Erro", 2: "Erro"})
        q15 = State(15, {0: "Erro", 1: "Erro", 2: "Erro"})
        q16 = State(16, {0: "Erro", 1: "Erro", 2: "Erro"})

        q17 = State(17, {0: 14, 1: 14, 2: 14})

        q18 = State(18, {0: 14, 1: 15, 2: 14})

        q19 = State(19, {0: 10, 1: 11, 2: 13})
        q20 = State(20, {0: 13, 1: 10, 2: 11})
        q21 = State(21, {0: 11, 1: 13, 2: 10})

        q22 = State(22, {0: 12, 1: 11, 2: 30})
        q23 = State(23, {0: 30, 1: 12, 2: 11})
        q24 = State(24, {0: 11, 1: 30, 2: 12})

        q25 = State(25, {0: 14, 1: 14, 2: 15})
        q26 = State(26, {0: 15, 1: 14, 2: 14})

        q27 = State(27, {0: 16, 1: 16, 2: 15})
        q28 = State(28, {0: 15, 1: 16, 2: 16})
        q29 = State(29, {0: 16, 1: 15, 2: 16})

        q30 = State(30, {0: 31, 1: 31, 2: 31})
        q31 = State(31, {0: 16, 1: 16, 2: 16})

        q32 = State(32, {0: 15, 1: 16, 2: 14})
        q33 = State(33, {0: 14, 1: 15, 2: 16})
        q34 = State(34, {0: 16, 1: 14, 2: 15})

        states = [
            q0,
            q1,
            q2,
            q3,
            q4,
            q5,
            q6,
            q7,
            q8,
            q9,
            q10,
            q11,
            q12,
            q13,
            q14,
            q15,
            q16,
            q17,
            q18,
            q19,
            q20,
            q21,
            q22,
            q23,
            q24,
            q25,
            q26,
            q27,
            q28,
            q29,
            q30,
            q31,
            q32,
            q33,
            q34,
        ]
        self.actual = 0
        self.states = states

    def get_result(self, domain1, domain2):
        for i in range(3):
            self.actual = self.states[self.actual].get_next(domain1[i])
            self.actual = self.states[self.actual].get_next(domain2[i])
        match self.actual:
            case 16:
                return "Domain 1"
            case 15:
                return "Draw"
            case 14:
                return "Domain 2"
