class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        total = 0
        
        for i in range(n):
            if i < n - 1 and s[i] == 'I' and (s[i + 1] == 'V' or s[i + 1] == 'X'):
                total -= 1
            elif i < n - 1 and s[i] == 'X' and (s[i + 1] == 'L' or s[i + 1] == 'C'):
                total -= 10
            elif i < n - 1 and s[i] == 'C' and (s[i + 1] == 'D' or s[i + 1] == 'M'):
                total -= 100
            else:
                if s[i] == 'I':
                    total += 1
                elif s[i] == 'V':
                    total += 5
                elif s[i] == 'X':
                    total += 10
                elif s[i] == 'L':
                    total += 50
                elif s[i] == 'C':
                    total += 100
                elif s[i] == 'D':
                    total += 500
                elif s[i] == 'M':
                    total += 1000

        return total