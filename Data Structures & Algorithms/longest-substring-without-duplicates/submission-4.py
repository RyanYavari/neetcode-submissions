class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''

        find longest substring -> sliding windows
        without duplicates -> set

        visited = set()

        longest = 0

        l, r = 0, 0

        for r in range(len(s)):

            while s[r] in set:
                remove l from set
                l++
            
            # at this point, no duplicates, add s[r] and log length
        



        z   x   y   z   x   y   z
            l
                    r
        longest = 3
        visited = xyz

        '''
        
        visited = set()
        longest = 0
        l, r = 0, 0

        for r in range(len(s)):
            


            while s[r] in visited: #if s[r] is in visited, increment l until s[r] not in set 
                visited.remove(s[l])
                l += 1
            visited.add(s[r])
            longest = max(longest, len(visited))
            
        return longest



            



            










    