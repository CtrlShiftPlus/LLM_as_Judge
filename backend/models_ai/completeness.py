from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
import re


class CompletenessJudge:

    def __init__(self):

        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    def split_prompt(self, prompt):

        prompt = prompt.replace("\n", " ")

        parts = re.split(r",| and ", prompt)

        stop = {
            "explain",
            "describe",
            "tell",
            "list",
            "compare",
            "using",
            "about",
            "with",
            "the",
            "a",
            "an",
            "advantages",
            "disadvantages",
            "of"
        }

        topics = []

        for part in parts:

            words = []

            for word in part.split():

                if word.lower() not in stop:
                    words.append(word)

            topic = " ".join(words).strip()

            if len(topic) > 2:
                topics.append(topic)

        return topics

    def evaluate(
        self,
        prompt,
        response
    ):

        topics = self.split_prompt(prompt)

        response_embedding = self.model.encode(
            response,
            convert_to_tensor=True
        )

        covered = []

        missing = []

        similarities = []

        for topic in topics:

            topic_embedding = self.model.encode(
                topic,
                convert_to_tensor=True
            )

            similarity = float(
                cos_sim(
                    topic_embedding,
                    response_embedding
                )[0][0]
            )

            similarities.append(similarity)

            if similarity >= 0.45:

                covered.append({
                    "topic": topic,
                    "similarity": round(similarity, 3)
                })

            else:

                missing.append({
                    "topic": topic,
                    "similarity": round(similarity, 3)
                })

        if len(topics) == 0:

            score = 100

        else:

            score = round(
                len(covered)
                /
                len(topics)
                *
                100
            )

        if score >= 90:

            status = "PASS"
            risk = "Low"

        elif score >= 70:

            status = "WARNING"
            risk = "Medium"

        else:

            status = "FAIL"
            risk = "High"

        if len(missing) == 0:

            explanation = (
                "The response covers every requested topic."
            )

            recommendation = (
                "No improvement required."
            )

        else:

            explanation = (
                f"The response covers {len(covered)} of "
                f"{len(topics)} requested topics."
            )

            recommendation = (
                "Include the missing topics in the response."
            )

        confidence = round(
            sum(similarities) / max(len(similarities), 1),
            3
        )

        return {

            "judge": "Completeness",

            "score": score,

            "weight": 20,

            "weighted_score": round(
                score * 0.20,
                2
            ),

            "status": status,

            "risk": risk,

            "confidence": confidence,

            "explanation": explanation,

            "recommendation": recommendation,

            "evidence": {

                "covered_topics": covered,

                "missing_topics": missing

            }

        }