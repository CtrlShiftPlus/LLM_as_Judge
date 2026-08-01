class ConsensusEngine:

    def calculate(self, scores):

        if len(scores) == 0:
            return 0

        return round(

            sum(scores) / len(scores),

            2

        )