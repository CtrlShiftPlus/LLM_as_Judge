from models_ai.hallucination import HallucinationJudge

judge = HallucinationJudge()

result = judge.evaluate(
    "Explain machine learning.",
    "Machine learning is a field of AI where systems learn from data."
)

print(result)