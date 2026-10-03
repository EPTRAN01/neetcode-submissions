class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #goal use subtraction to get the needed two elements that add up to the List

  
        #target - one of the elements then seeing if the rest of it matches 
        #if it doesnt it moves on to the next without going over it again
        #probably need a hashmap for the key 
        # for an example 7- one element and it gives a value then i find it if its in num then i find the two postions as the output 

        hashmap = {}
        for i, n in enumerate(nums):
            prediction = target - n
            if prediction in hashmap:
                return [hashmap[prediction], i]
            hashmap[nums[i]] = i
        