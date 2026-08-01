class ConsensusJudge:

    def evaluate(self, judge_results):

        total_weighted_score = 0

        strengths = []

        weaknesses = []

        recommendations = []

        for result in judge_results:

            total_weighted_score += result["weighted_score"]

            if result["status"] == "PASS":

                strengths.append(
                    result["judge"]
                )

            else:

                weaknesses.append(
                    result["judge"]
                )

                recommendations.append(
                    result["recommendation"]
                )

        final_score = round(total_weighted_score)

        if final_score >= 85:

            status = "PASS"

            risk = "Low"

        elif final_score >= 70:

            status = "WARNING"

            risk = "Medium"

        else:

            status = "FAIL"

            risk = "High"

        return {

            "judge": "Final Consensus",

            "overall_score": final_score,

            "overall_status": status,

            "overall_risk": risk,

            "strengths": strengths,

            "weaknesses": weaknesses,

            "recommendations": recommendations,

            "summary": (
                f"{len(strengths)} judges passed and "
                f"{len(weaknesses)} judges reported issues."
            )

        }