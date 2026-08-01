import joblib
import numpy as np

model = joblib.load("trained_models/toxicity_model.pkl")
vectorizer = joblib.load("trained_models/toxicity_vectorizer.pkl")


class ToxicityJudge:

    def evaluate(self, text):

        X = vectorizer.transform([text])

        prediction = model.predict(X)[0]

        decision = model.decision_function(X)

        if isinstance(decision, np.ndarray):
            confidence = float(abs(decision[0]))
        else:
            confidence = float(abs(decision))

        confidence = min(confidence / 5, 1.0)

        if prediction == 1:

            score = 20
            status = "FAIL"
            risk = "High"

            explanation = (
                "Toxic language detected."
            )

            recommendation = (
                "Remove offensive or abusive language."
            )

        else:

            score = 100
            status = "PASS"
            risk = "Low"

            explanation = (
                "No toxic language detected."
            )

            recommendation = (
                "No changes required."
            )

        return {

            "judge": "Toxicity",

            "score": score,

            "weight": 20,

            "weighted_score": round(
                score * 0.20,
                2
            ),

            "status": status,

            "risk": risk,

            "confidence": round(
                confidence,
                2
            ),

            "explanation": explanation,

            "recommendation": recommendation,

            "evidence": {

                "prediction":
                "Toxic"
                if prediction == 1
                else
                "Non Toxic"

            }

        }