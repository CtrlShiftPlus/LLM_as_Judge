from models_ai.completeness import CompletenessJudge

judge = CompletenessJudge()

print(
    judge.evaluate(
        "Explain Python and Java",
        "Python is an interpreted programming language."
    )
)