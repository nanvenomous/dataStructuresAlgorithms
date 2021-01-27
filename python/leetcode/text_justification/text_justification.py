# nOpeneins = 3
# extraSpaces = 7
# [' ', ' ', ' '] 

from typing import List
class TextJustification:
    def __init__(self) -> None:
        self.words = None
        self.maxWidth = 0

    def _getLine(self, s, e, curLineLen):
        words = self.words[s:e]
        nWords = len(words)
        nOpenings = nWords - 1
        extraSpaces = self.maxWidth - curLineLen
        evenSpaces = int(extraSpaces/nOpenings) + 1
        additionalSpaces = extraSpaces%nOpenings
        line = []
        for i in range(nOpenings):
            line.append(words[i])
            width = evenSpaces + 1 if additionalSpaces else evenSpaces
            emptySpace = [' ' for _ in range(width)]
            line += emptySpace
            if additionalSpaces > 0: additionalSpaces -= 1
        line.append(words[i + 1])
        return ''.join(line)

    def _measureLine(self, s):
        curLineLen = 0
        potLineLen = len(self.words[s])
        potEnd = s + 1
        # ensure potential length is not more than maximum allowed length
        while potLineLen < self.maxWidth:
            curLineLen = potLineLen
            # potLineLen is current line length + a space and the length of the next word
            potLineLen = curLineLen + 1 + len(self.words[potEnd])
            potEnd += 1
        # make the line with the gathered information
        line = self._getLine(
            s=s,
            e=potEnd-1,
            curLineLen=curLineLen
            )
        return line, potEnd - 1

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        self.words = words
        self.maxWidth = maxWidth
        s = 0
        line, i = self._measureLine(
            s=s
            )
        print()
        print(line)
        print(i)
        return 0