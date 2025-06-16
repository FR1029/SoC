class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = count = 0

        for i in range(len(t)):
            if j < len(s) and t[i] == s[j]:
                count += 1
                j += 1
            i += 1
        if count == len(s):
            return True
        
        return False