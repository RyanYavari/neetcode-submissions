class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        '''
        anagram = string contains exact same chars as other string
            in other words, strings have same freq of chars
        
        we need a hashMap to map frequencies of characters in the following key:value order
            char : count
        
        if s & t have the same hashMap frequencies then they're both anagrams
            in other words, if hashMapS == hashMapT, return True
        
        pseudo:
        hashMapS = {}
        hashMapT = {}

        for char in s:
            add to hashMap
        
        for char in t:
            add to hashMap
        
        if hashMapS == hashMapT:
            return True
        return False



        '''


        hashMapS = {}
        hashMapT = {}

        for char in s:
            hashMapS[char] = hashMapS.get(char, 0) + 1
        
        for char in t:
            hashMapT[char] = hashMapT.get(char, 0) + 1
        
        if hashMapS == hashMapT:
            return True
        return False
        
        