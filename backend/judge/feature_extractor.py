"""
Feature Extraction Module

This module extracts all features required by the
AI Judge System.

Current Features

1. Character Count
2. Word Count
3. Sentence Count
4. Average Word Length
5. Response Length Category

Later we will add

✓ TF-IDF
✓ Sentence Embeddings
✓ Readability
✓ Named Entities
"""

import re


class FeatureExtractor:

    def clean_text(self, text):

        if text is None:
            return ""

        text = text.strip()

        text = re.sub(r"\s+", " ", text)

        return text


    def word_count(self, text):

        return len(text.split())


    def sentence_count(self, text):

        return len(
            re.findall(r"[.!?]", text)
        )


    def character_count(self, text):

        return len(text)


    def average_word_length(self, text):

        words = text.split()

        if len(words) == 0:
            return 0

        total = sum(len(w) for w in words)

        return round(total / len(words), 2)


    def extract(self, response):

        response = self.clean_text(response)

        return {

            "characters": self.character_count(response),

            "words": self.word_count(response),

            "sentences": self.sentence_count(response),

            "avg_word_length": self.average_word_length(response)

        }