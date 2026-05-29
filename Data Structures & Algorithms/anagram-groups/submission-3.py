class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ansdict = defaultdict(list)

        for word in strs:
            mapping = [0] * 26
            for letter in word:
                mapping[ord(letter) - ord('a')] += 1
            ansdict[tuple(mapping)].append(word)
        
        return list(ansdict.values())
