from models_ai.toxicity import ToxicityJudge

judge = ToxicityJudge()

print(
    judge.evaluate(
        "I disagree with your opinion because the facts are incorrect."
    )
)

print(
    judge.evaluate(
        "You are an idiot."
    )
)