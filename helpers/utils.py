import re

class Utils:
    def __init__(self):
        pass

    # Return the frequency of a word in a string or a list
    def word_frequency(self, word: str, text) -> int:
        if isinstance(text, str):
            return sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), text))
        return text.count(word)