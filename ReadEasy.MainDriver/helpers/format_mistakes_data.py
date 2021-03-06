import json

class FormatMistakesData():
    def __init__(self) -> None:
        self._replacements = {}
        self._insertions = []
        self._omissions = {}
        self._misplacement = []

    def catch_replacements(self, word: str, index: int):
        self._replacements[index] = word

    def catch_insertions(self, word: str):
        self._insertions.append(word)

    def catch_omission(self, word: str, index: int):
        self._omissions[index] = word

    def catch_misplacement(self, word: str):
        self._misplacement.append(word)

    def toJSONString(self):
        data = {
            'replacements': self._replacements,
            'insertions': self._insertions,
            'omissions': self._omissions,
            'misplacements': self._misplacement
        }
        read_correctly = False
        if len(self._replacements) + len(self._insertions) + len(self._omissions) + len(self._misplacement)== 0:
            read_correctly = True
        return json.dumps(data), read_correctly