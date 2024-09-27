from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Initialize an array to count bits
        bit_count = [0] * 32  # 32 bits for integer representation
        
        # Count the bits for each number
        for num in nums:
            for i in range(32):
                if num & (1 << i):
                    bit_count[i] += 1
        
        # Construct the result from the bit counts
        result = 0
        for i in range(32):
            # Only include bits that are not a multiple of 3
            if bit_count[i] % 3:
                result |= (1 << i)
        
        # Handle the case where the result is negative
        # If the 31st bit is set, we need to convert it to a negative number
        if bit_count[31] % 3:  # If the sign bit is part of the unique number
            result -= (1 << 32)
        
        return result

# Example usage:
solution = Solution()
print(solution.singleNumber([2, 2, 3, 2]))  # Output: 3
print(solution.singleNumber([0, 1, 0, 1, 0, 1, 99]))  # Output: 99
