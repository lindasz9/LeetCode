class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0  # Total number of valid ways to reach the top

        # Recursive helper function to try steps from current count
        def step(cnt):
            nonlocal count
            if cnt > n:
                return  # Exceeded total steps, not a valid path
            if cnt == n:
                count += 1  # Reached exactly n steps, valid path found
                return
            step(cnt + 1)  # Take 1 step
            step(cnt + 2)  # Take 2 steps

        step(0)  # Start from step 0
        return count  # Return total number of ways
