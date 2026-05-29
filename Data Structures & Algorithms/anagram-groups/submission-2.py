class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # def getContentDict(word: str) -> Dict:
        #     d = {}
        #     for letter in word:
        #         d[letter] = d.get(letter, 0) + 1
        #     return d
        
        # ansdict = {}
        # for word in strs:
        #     d = getContentDict(word)
        #     anskey = frozenset(d.items())
        #     if anskey in ansdict:
        #         ansdict[anskey].append(word)
        #     else:
        #         ansdict[anskey] = [word]
        # return list(ansdict.values())

        ansdict = defaultdict(list)

        for word in strs:
            mapping = [0] * 26
            for letter in word:
                mapping[ord(letter) - ord('a')] += 1
            ansdict[tuple(mapping)].append(word)
        
        return list(ansdict.values())

