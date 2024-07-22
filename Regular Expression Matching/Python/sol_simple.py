"""Regular Expression Matching(Leetcode Prob.10)
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
"""
#O(2^(n+m))
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        j,i = 0,0
        

        while i < n:
            if i + 1 < n and p[i + 1] == "*":
                # Handle the '*' 
                
                if j < m and (p[i] == s[j] or p[i] == "."):
                    # Try to match 0 or more characters
                    while j < m and (p[i] == s[j] or p[i] == "."):
                        if self.isMatch(s[j:], p[i + 2:]):
                            return True
                        j = j + 1
                    i = i +2  # Skip both the current character and '*'
                else:
                    # Skip the '*' 
                    i = i + 2
            elif j < m and (p[i] == s[j] or p[i] == "."):
                # Characters match or p[i] is '.'
                j = j + 1
                i = i + 1
            else:
                return False

        # Ensure full match of both string
        return j == m and i == n


