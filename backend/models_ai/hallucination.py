from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim


class HallucinationJudge:

    def __init__(self):
        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    def evaluate(self, prompt, response):

        prompt_embedding = self.model.encode(
            prompt,
            convert_to_tensor=True
        )

        response_embedding = self.model.encode(
            response,
            convert_to_tensor=True
        )

        similarity = float(
            cos_sim(
                prompt_embedding,
                response_embedding
            )[0][0]
        )

        score = round(similarity * 100)

        score = max(0, min(score, 100))

        if score >= 85:

            status = "PASS"
            risk = "Low"

            explanation = (
                "The response appears grounded in the user's prompt."
            )

            recommendation = (
                "No hallucination indicators detected."
            )

        elif score >= 65:

            status = "WARNING"
            risk = "Medium"

            explanation = (
                "The response is only partially grounded in the prompt."
            )

            recommendation = (
                "Verify important factual claims."
            )

        else:

            status = "FAIL"
            risk = "High"

            explanation = (
                "The response may contain hallucinated or unrelated information."
            )

            recommendation = (
                "Review the response for unsupported claims."
            )

        return {

            "judge": "Hallucination",

            "score": score,

            "weight": 20,

            "weighted_score": round(score * 0.20, 2),

            "status": status,

            "risk": risk,

            "confidence": round(similarity, 3),

            "explanation": explanation,

            "recommendation": recommendation,

            "evidence": {
                "semantic_similarity": round(similarity, 3)
            }

        }