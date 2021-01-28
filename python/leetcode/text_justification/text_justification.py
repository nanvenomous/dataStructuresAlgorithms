from typing import List
class TextJustification:
    def __init__(self) -> None:
        self.words = None
        self.maxWidth = 0
        self.finished = False

    def _getLine(self, s, e, curLineLen):
        words = self.words[s:e]
        # left justify
        if self.finished:
            lineLst = []
            for wd in words:
                lineLst += [wd, ' ']
            lineLst.pop()
            width = (self.maxWidth - curLineLen)
            emptySpace = [' ' for _ in range(width)]
            lineLst += emptySpace
            return ''.join(lineLst)
        nWords = len(words)
        if not nWords == 1:
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
        else:
            word = words[0]
            remainingCharacters = self.maxWidth - len(word)
            emptySpace = [' ' for _ in range(remainingCharacters)]
            words += emptySpace
            return ''.join(words)

    def _measureLine(self, s):
        curLineLen = 0
        if not s > len(self.words) - 1:
            potLineLen = len(self.words[s])
        else:
            self.finished = True
            return
        potEnd = s + 1
        # ensure potential length is not more than maximum allowed length
        while potLineLen <= self.maxWidth:
            curLineLen = potLineLen
            if not potEnd > len(self.words) - 1:
                # potLineLen is current line length + a space and the length of the next word
                potLineLen = curLineLen + 1 + len(self.words[potEnd])
                potEnd += 1
            else:
                self.finished = True
                potEnd += 1
                break
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
        justifiedText = []
        s = 0
        while not self.finished:
            line, s = self._measureLine(
                s=s
                )
            justifiedText.append(line)
        return justifiedText