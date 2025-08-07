class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths differ, cannot be anagrams
        if len(s) != len(t):
            return False
        
        sht, tht = {}, {}  # Dictionaries to count character frequencies
        
        # Count characters in both strings
        for c in range(len(s)):
            sht[s[c]] = sht.get(s[c], 0) + 1
            tht[t[c]] = tht.get(t[c], 0) + 1
        
        # Compare frequency dictionaries to confirm anagram
        return sht == tht
