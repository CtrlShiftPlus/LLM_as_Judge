from models_ai.consensus import ConsensusJudge

judge = ConsensusJudge()

results = [

    {
        "judge":"Relevance",
        "weighted_score":18,
        "status":"PASS",
        "recommendation":""
    },

    {
        "judge":"Completeness",
        "weighted_score":16,
        "status":"PASS",
        "recommendation":""
    },

    {
        "judge":"Hallucination",
        "weighted_score":17,
        "status":"PASS",
        "recommendation":""
    },

    {
        "judge":"Readability",
        "weighted_score":8,
        "status":"WARNING",
        "recommendation":"Simplify language."
    },

    {
        "judge":"Toxicity",
        "weighted_score":20,
        "status":"PASS",
        "recommendation":""
    },

    {
        "judge":"Consistency",
        "weighted_score":9,
        "status":"PASS",
        "recommendation":""
    }

]

print(
    judge.evaluate(results)
)