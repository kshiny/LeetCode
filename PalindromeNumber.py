class Solution:
    # bool is data type represents true and false.
    def isPalindrome(self, x: int) -> bool:
            x = list(str(x))
            
            return x == x[::-1]