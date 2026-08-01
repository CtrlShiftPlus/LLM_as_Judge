class Explainability:

    def generate(self, score):

        if score >= 90:

            return "Excellent response."

        elif score >= 75:

            return "Good response with minor improvements."

        elif score >= 60:

            return "Average response. Some issues detected."

        else:

            return "Poor response. Significant improvements required."