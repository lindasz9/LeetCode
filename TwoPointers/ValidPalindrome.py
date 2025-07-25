class Solution:
    # Determines if the given string is a palindrome, considering only alphanumeric characters and ignoring cases
    def isPalindrome(self, s: str) -> bool:
        def isalpnum(c):
            # Checks if the character is alphanumeric using ASCII values
            if ord('0') <= ord(c) <= ord('9'):
                return True
            if ord('a') <= ord(c) <= ord('z'):
                return True
            if ord('A') <= ord(c) <= ord('Z'):
                return True
            return False

        l, r = 0, len(s) - 1  # Initialize two pointers at the start and end of the string

        while l < r:
            if not isalpnum(s[l]):
                l += 1  # Skip non-alphanumeric characters from the left
            elif not isalpnum(s[r]):
                r -= 1  # Skip non-alphanumeric characters from the right
            elif s[l].lower() == s[r].lower():
                l += 1  # Characters match, move both pointers inward
                r -= 1
            else:
                return False  # Mismatch found, not a palindrome

        return True  # All characters matched, it's a palindrome
