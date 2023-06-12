"""
Contains string similarity matching methods
"""

from difflib import SequenceMatcher

def similar(str1: str, str2: str) -> float:
    """Returns the similarity ratio between two strings"""
    return SequenceMatcher(None, str1, str2).ratio()

print(similar("Taon Portal", "Town Portal"))