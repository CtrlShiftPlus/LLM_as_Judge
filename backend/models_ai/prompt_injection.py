import os
import joblib


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "trained_models",
    "prompt_injection_model.pkl"
)

VECTORIZER_PATH = os.path.join(
    BASE_DIR,
    "trained_models",
    "prompt_injection_vectorizer.pkl"
)


class PromptInjectionJudge:

    def __init__(self):
        self.model = joblib.load(MODEL_PATH)
        self.vectorizer = joblib.load(VECTORIZER_PATH)

    def evaluate(self, text):

        vector = self.vectorizer.transform([text])

        prediction = int(self.model.predict(vector)[0])

        confidence = 0.95

        if prediction == 1:
            return {
                "judge": "Prompt Injection",
                "score": 15,
                "status": "FAIL",
                "risk": "High",
                "confidence": confidence,
                "explanation": "The prompt appears to contain prompt injection patterns attempting to override instructions.",
                "recommendation": "Reject this prompt or sanitize it before sending it to the LLM.",
                "evidence": [
                    "Detected prompt injection pattern"
                ]
            }

        return {
            "judge": "Prompt Injection",
            "score": 100,
            "status": "PASS",
            "risk": "Low",
            "confidence": confidence,
            "explanation": "No prompt injection behavior detected.",
            "recommendation": "Prompt is safe to process.",
            "evidence": []
        }