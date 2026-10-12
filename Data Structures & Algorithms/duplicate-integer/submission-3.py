class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #the problem ask me given an array which is a list, if there is a duplicate then it returns true, otherwise it returns false
        #what pattern can I use to attend this?
        #I can plug it in a hashmap, since i can compare it in a key
        #initialize a hashmap
        #instead of hashmap since im looking for already exisitng values i have to do a set and it has a o(1) time complexity 
       # for n in nums:
       #     if statement in the hashmap then it has to return true since it is in the list alr

        #    else initialize it then increment n to move through num

        #    then outside scope return false
            
            
        seen = set()

        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)
        return False
            