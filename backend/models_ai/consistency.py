class ConsistencyJudge:

    def evaluate(self, judge_results):

        scores = []

        disagreements = []

        for result in judge_results:

            scores.append(result["score"])

            if result["status"] != "PASS":
                disagreements.append(result["judge"])

        consistency_score = round(
            sum(scores) / len(scores)
        )

        if consistency_score >= 85:

            status = "PASS"
            risk = "Low"

        elif consistency_score >= 70:

            status = "WARNING"
            risk = "Medium"

        else:

            status = "FAIL"
            risk = "High"

        if len(disagreements) == 0:

            explanation = (
                "All judges agree that the response is of high quality."
            )

            recommendation = (
                "No consistency issues detected."
            )

        else:

            explanation = (
                "Some judges reported quality issues."
            )

            recommendation = (
                "Review the judges that reported warnings or failures."
            )

        return {

            "judge": "Consistency",

            "score": consistency_score,

            "weight": 10,

            "weighted_score": round(
                consistency_score * 0.10,
                2
            ),

            "status": status,

            "risk": risk,

            "confidence": round(
                consistency_score / 100,
                2
            ),

            "explanation": explanation,

            "recommendation": recommendation,

            "evidence": {

                "judges_checked": [
                    j["judge"]
                    for j in judge_results
                ],

                "disagreements": disagreements

            }

        }