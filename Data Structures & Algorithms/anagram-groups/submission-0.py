class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
 #       O(n*m) solution:
#1. result = defaultdict(list).
#2. loop through each string in list of strings
#3. create a count array of 26, representing each letter in alphabet
#4. for each character in string, count frequency of letters
 #      count[char] = frequency
#5. append string to result where key is the count array and values are the list of strings
#6. return result.values()

        result = defaultdict(list)

        for s in strs:
            count = [0]*26 # represents a...z
            for char in s:
                count[ord(char) - ord("a")] += 1
            
            result[tuple(count)].append(s)
        return list(result.values())
            
