class Solution:
    def __init__(self):
        self.delimiter = "😀"
        self.countDelim = "😃"

    def encode(self, strs: List[str]) -> str:
        return str(len(strs)) + self.countDelim + self.delimiter.join(strs)

    def decode(self, s: str) -> List[str]:
        countStr, strs = s.split(self.countDelim)
        count = int(countStr)
        return strs.split(self.delimiter) if count > 0 else []
