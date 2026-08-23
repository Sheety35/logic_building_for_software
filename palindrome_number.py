class Solution:
    def isPalindrome(self, x: int) -> bool:
        m = x
        n=0
        while x > 0:
            d = x % 10
            n = n * 10 + d
            x //= 10
        
        if n == m: return True
        return False
