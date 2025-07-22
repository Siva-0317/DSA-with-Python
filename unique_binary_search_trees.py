#Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
class Solution:
    def numTrees(self, n: int) -> int:
        # Initialize a list to store the number of unique BSTs for each count of nodes
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: one empty tree
        
        # Fill the dp array using the Catalan number formula
        """Catalan number formula and explanation: C(n) = sum(C(i-1) * C(n-i) for i in range(1, n+1))
        explained:
        The number of unique BSTs with n nodes can be calculated using the Catalan number formula"""
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        
        return dp[n]
# Example usage:
sol = Solution()
print(sol.numTrees(3))