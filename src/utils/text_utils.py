import re
from collections import Counter


def get_words_from_string(string: str) -> list[str]:
    return re.findall(r'\b\w+\b', string.lower())


def words_counter(string: str) -> Counter[str]:
    return Counter(get_words_from_string(string))
