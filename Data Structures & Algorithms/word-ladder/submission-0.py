class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        

        '''

        for every word, find all of its patterns
        then for every pattern, find the words that will fit that pattern
        that is your adjacency list. an adjacency list of patterns


        then do simple bfs 


        patterns[hot] = *ot, h*t, ho*






        '''


        wordList.append(beginWord)

        patterns = collections.defaultdict(list) #since we dont know how many patterns we will have make a default dict

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                patterns[pattern].append(word)



        visit = set()

        queue = deque()

        length = 1

        queue.append(beginWord)
        visit.add(beginWord)

        while(queue):
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return length

                # now we have to search for every neighbor of word
                # we find word's neighbors by finding all of its patterns
                #then after finding its patterns, we add the patterns' words to queue

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nei in patterns[pattern]:
                        if nei not in visit:
                            queue.append(nei)
                            visit.add(nei)
            
            length += 1
        
        return 0
        
        


        
        