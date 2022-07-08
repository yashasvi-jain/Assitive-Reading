import re

class Utils:
    def __init__(self):
        pass

    def word_frequency(self, word: str, text: list) -> int:
        # count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), text))
        # return count
        return text.count(word)