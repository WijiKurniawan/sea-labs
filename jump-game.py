class Solution:
    def canReach(self, nums):
        # Initialize the farthest position we can reach
        farthest = 0
        
        # Iterate through the array
        for i in range(len(nums)):
            # If the current index is beyond the farthest position we can reach, return False
            if i > farthest:
                return False
            
            # Update the farthest position we can reach
            farthest = max(farthest, i + nums[i])
            
            # If the farthest position we can reach is beyond or at the last index, return True
            if farthest >= len(nums) - 1:
                return True
        
        # If we finish the loop without returning False, return True
        return True