class Solution:
    # Checks if there are any duplicate elements in the list
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # Stores unique elements we've encountered so far
        
        for i in nums:
            if i in seen:
                return True  # Duplicate found, return early for efficiency
            seen.add(i)  # Track the current number
        
        return False  # No duplicates found after checking all elements
