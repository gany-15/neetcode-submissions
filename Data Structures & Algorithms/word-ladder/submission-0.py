class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set()
        wordToWild = defaultdict(list)
        wildToWord = defaultdict(list)

        wordList.append(beginWord)

        for word in wordList:
            if word not in wordToWild:
                for i in range(len(word)):
                    wildcard = word[:i] + '*' + word[i+1:]
                    wordToWild[word].append(wildcard)
                    wildToWord[wildcard].append(word)
        
        ans = 0
        q = deque()
        q.append(beginWord)
        visited.add(beginWord)
        
        while q:
            length = len(q)
            ans += 1
            for i in range(length):
                word = q.popleft()

                if word == endWord:
                    return ans
                
                wildcards = wordToWild[word]
                for wc in wildcards:
                    if wc not in visited:
                        visited.add(wc)
                        for ww in wildToWord[wc]:
                            if ww not in visited:
                                visited.add(ww)
                                q.append(ww)
        
        return 0