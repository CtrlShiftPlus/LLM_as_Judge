from models_ai.readability import ReadabilityJudge

judge = ReadabilityJudge()

print(
    judge.evaluate(
        "Machine learning is a branch of artificial intelligence. It allows computers to learn from data instead of being explicitly programmed."
    )
)