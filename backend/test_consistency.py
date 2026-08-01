from models_ai.consistency import ConsistencyJudge

judge = ConsistencyJudge()

results = [

    {
        "judge":"Relevance",
        "score":90,
        "status":"PASS"
    },

    {
        "judge":"Completeness",
        "score":80,
        "status":"WARNING"
    },

    {
        "judge":"Hallucination",
        "score":88,
        "status":"PASS"
    },

    {
        "judge":"Readability",
        "score":75,
        "status":"WARNING"
    },

    {
        "judge":"Toxicity",
        "score":100,
        "status":"PASS"
    }

]

print(
    judge.evaluate(results)
)