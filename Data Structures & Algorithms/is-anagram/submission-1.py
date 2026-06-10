class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # put both strings into arrays
        # sort arrays in ascending ASCII value
        # if arrays are equal, return true
        # else, return false

        if len(s) != len(t):
            return False

        s_arr = []
        t_arr = []

        for i in range(len(s)):
            s_arr.append(s[i])
            t_arr.append(t[i])
        
        s_arr.sort()
        t_arr.sort()

        for i in range(len(s_arr)):
            if s_arr[i] != t_arr[i]:
                return False
        return True


        
