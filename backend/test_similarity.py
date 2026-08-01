from models_ai.similarity import SimilarityJudge

judge = SimilarityJudge()

print(
    judge.evaluate(
        "Explain Python",
        "Python is a programming language."
    )
)