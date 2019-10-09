class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ 
            Inputs - List of ints, a target sum
            Goal/Output - List containing indices for the two numbers which add to the target
            Assumptions - Exactly one solution will exist
            Thoughts: 
            We could bruteforce by nested looping over list, checking for two values to equal the target and return the indices.
            This solution, taking nested loops over n, will give us O(n^2)

            Seeking a better solution, we might uncover that we can keep a lookup of the compliments we are seeking.
            Then for any given value, we see if it is a complement we are seeking and the index which put out the request.
            Otherwise, we list the current value's compliment as the key and the index of this value as the value so a future number might uncover it.
            This better solution will only take a single pass through the list and with a performant lookup table, will be O(n)
        """

        """ Sudo Code
        Check if value is a previous complement - if so return value and current index
        else add compliement, index to lookup
        """
        
        lookup = {}
        for index in range(len(nums)):
            num = nums[index]
            
            if num in lookup:
                compliment_index = lookup[num]
                return [index, compliment_index]
            
            else:
                compliment = target - num
                lookup[compliment] = index
