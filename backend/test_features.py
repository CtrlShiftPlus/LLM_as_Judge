from judge.feature_extractor import FeatureExtractor

extractor = FeatureExtractor()

response = """
Artificial Intelligence is the simulation
of human intelligence using machines.
"""

print(extractor.extract(response))