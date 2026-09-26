class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        '''

        anagram = same freq hashmap/array of char count

        groupAnagrams = {}

        1. calculate char freq of each string in a count arr
        2. convert to tuple
        3. check if tuple is in groupAnagrams
            3.1 if true -> add string to value list in groupAnagrams[tuple(count)]
            3.1 if false -> add key and value (string) to groupAnagrams
        4. return list(groupAnagrams.values()) # cast into a list

        '''

        groupAnagrams = {}

        for s in strs:
            #calc char freq
            count = [0]*26

            for char in s:
                count[ord(char)-ord('a')] += 1
            
            if tuple(count) in groupAnagrams:
                groupAnagrams[tuple(count)].append(s)
            else:
                groupAnagrams[tuple(count)] = [s]
            
        return list(groupAnagrams.values())









        