class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #the problem ask if a value appears more than once then it appears true
        #other wise if it only appears once its false


        #first I want it to go through the list
        #how i will go through this problem is that I will make it into a key and plug it in
        key = set()
        for n in nums:  #I want it to loop through the list for n. If n is not in the key it will initialize it and put it the set
            if n in key:
                return True
            key.add(n)
        return False
       

            