class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getContentDict(word: str) -> Dict:
            d = {}
            for letter in word:
                d[letter] = d.get(letter, 0) + 1
            return d
        
        ansdict = {}
        for word in strs:
            d = getContentDict(word)
            anskey = frozenset(sorted(d.items()))
            if anskey in ansdict:
                ansdict[anskey].append(word)
            else:
                ansdict[anskey] = [word]
        return list(ansdict.values())

