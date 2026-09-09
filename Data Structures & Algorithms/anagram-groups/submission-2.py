class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        '''

        anagrams = two strings having the same character frequencies

        group all strings with same freq hashmaps into the same list

        
        groupAnagrams = {}

        for s in strs
            count = [0]*26

            for i in range(len(s)):
                count[ord(s[i]) - ord('a')] += 1
            
            # we got frequencies of each str, now group them in hashmap
            #key has to be immutable -> tuple

            groupAnagrams[tuple(count)].append(s)
        
        retrun groupAnagrams.values()

        

        '''

        groupAnagrams = {}

        for s in strs:
            count = [0]*26

            for i in range(len(s)):
                count[ord(s[i]) - ord('a')] += 1
            
            # we got frequencies of each str, now group them in hashmap
            #key has to be immutable -> tuple

            if tuple(count) not in groupAnagrams:
                groupAnagrams[tuple(count)] = []

            groupAnagrams[tuple(count)].append(s)
        
        return list(groupAnagrams.values())
        


