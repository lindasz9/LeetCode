class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}  # Dictionary to group anagrams by character frequency signature

        for s in strs:
            abc = [0] * 26  # Frequency count for each character (a–z)
            for c in s:
                cc = ord(c) - ord("a")  # Get index for character
                abc[cc] += 1            # Increment count at corresponding index
            
            key = tuple(abc)  # Convert list to tuple to use as dict key

            if key not in res:
                res[key] = []  # Initialize list for this anagram group
            res[key].append(s)  # Append original string to the group
        
        # Return all grouped anagrams as a list of lists
        return [v for v in res.values()]
