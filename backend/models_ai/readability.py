import re


class ReadabilityJudge:

    def count_words(self, text):

        words = re.findall(
            r"\b[a-zA-Z]+\b",
            text
        )

        return len(words)

    def count_sentences(self, text):

        sentences = re.split(
            r"[.!?]+",
            text
        )

        sentences = [
            s.strip()
            for s in sentences
            if s.strip()
        ]

        return len(sentences)

    def count_syllables(self, word):

        word = word.lower()

        vowels = "aeiou"

        count = 0

        previous_vowel = False

        for char in word:

            is_vowel = char in vowels

            if is_vowel and not previous_vowel:
                count += 1

            previous_vowel = is_vowel

        if word.endswith("e") and count > 1:
            count -= 1

        return max(count, 1)

    def calculate_score(self, text):

        words = re.findall(
            r"\b[a-zA-Z]+\b",
            text.lower()
        )

        sentences = self.count_sentences(text)

        if len(words) == 0:
            return 0, 0, 0

        syllables = sum(
            self.count_syllables(w)
            for w in words
        )

        avg_sentence_length = (
            len(words)
            /
            max(sentences, 1)
        )

        avg_syllables = (
            syllables
            /
            len(words)
        )

        score = (
            206.835
            -
            (1.015 * avg_sentence_length)
            -
            (84.6 * avg_syllables)
        )

        score = round(
            max(
                0,
                min(
                    100,
                    score
                )
            )
        )

        return score, len(words), sentences

    def evaluate(self, response):

        score, words, sentences = self.calculate_score(
            response
        )

        if score >= 80:

            status = "PASS"
            risk = "Low"

            explanation = (
                "The response is easy to read."
            )

            recommendation = (
                "No readability improvements required."
            )

        elif score >= 60:

            status = "WARNING"
            risk = "Medium"

            explanation = (
                "The response is readable but somewhat complex."
            )

            recommendation = (
                "Simplify long sentences where possible."
            )

        else:

            status = "FAIL"
            risk = "High"

            explanation = (
                "The response is difficult to read."
            )

            recommendation = (
                "Use simpler language and shorter sentences."
            )

        return {

            "judge": "Readability",

            "score": score,

            "weight": 10,

            "weighted_score": round(score * 0.10, 2),

            "status": status,

            "risk": risk,

            "confidence": 1.0,

            "explanation": explanation,

            "recommendation": recommendation,

            "evidence": {

                "word_count": words,

                "sentence_count": sentences,

                "reading_score": score

            }

        }