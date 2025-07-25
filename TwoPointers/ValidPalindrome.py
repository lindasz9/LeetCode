class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isalpnum(c):
            if ord('0') <= ord(c) <= ord('9'):
                return True
            if ord('a') <= ord(c) <= ord('z'):
                return True
            if ord('A') <= ord(c) <= ord('Z'):
                return True
            return False

        l, r = 0, len(s) - 1
        while l < r:
            if not isalpnum(s[l]):
                l += 1
            elif not isalpnum(s[r]):
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True
