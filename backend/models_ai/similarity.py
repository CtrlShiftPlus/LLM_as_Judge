from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim


class SimilarityJudge:

    def __init__(self):

        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    def evaluate(
        self,
        prompt,
        response
    ):

        emb1 = self.model.encode(
            prompt,
            convert_to_tensor=True
        )

        emb2 = self.model.encode(
            response,
            convert_to_tensor=True
        )

        similarity = float(
            cos_sim(
                emb1,
                emb2
            )[0][0]
        )

        score = round(
            max(
                0,
                min(
                    similarity * 100,
                    100
                )
            )
        )

        if score >= 90:

            status = "PASS"
            risk = "Low"

            explanation = (
                "The response is highly aligned with the user prompt."
            )

            recommendation = (
                "No improvement required."
            )

        elif score >= 70:

            status = "WARNING"
            risk = "Medium"

            explanation = (
                "The response is generally relevant but could better match the prompt."
            )

            recommendation = (
                "Include more details requested in the prompt."
            )

        else:

            status = "FAIL"
            risk = "High"

            explanation = (
                "The response has low semantic similarity to the prompt."
            )

            recommendation = (
                "Rewrite the response to better answer the prompt."
            )

        return {

            "judge": "Similarity",

            "score": score,

            "weight": 10,

            "weighted_score": round(
                score * 0.10,
                2
            ),

            "status": status,

            "risk": risk,

            "confidence": round(
                similarity,
                3
            ),

            "explanation": explanation,

            "recommendation": recommendation,

            "evidence": {

                "semantic_similarity": round(
                    similarity,
                    3
                )

            }

        }