class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        minStr = min(strs, key=len)
        for i, j in enumerate(minStr):
            for other in strs:
                if other[i] != j:
                    return minStr[:i]
        return minStr