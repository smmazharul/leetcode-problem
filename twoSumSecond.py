class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0,len(numbers)-1

        while left<right:
            if numbers[left]+numbers[right]==target:
                return [left+1,right+1]
            elif numbers[left]+numbers[right]<target:
                left+=1
            else:
                right-=1


# here use two pointers to find the target sum
# since the array is sorted, we can move the left pointer to the right to increase the sum or move the right pointer to the left to decrease the sum
# time complexity is O(n)
# space complexity is O(1)
# Example usage:
# sol = Solution()
# print(sol.twoSum([2,7,11,15],9))  # Output: [1,2]
