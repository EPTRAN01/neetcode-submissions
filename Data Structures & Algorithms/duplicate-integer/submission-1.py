class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      
#I want it to go through the list then apply boolean to see if its true

#I have to compare values

#so i need a loop or hashmap 

#first step I need to get the values, and map it

#linked list method to go through the list is the kind of brute force method
#hashmap seems better for the time and space complexity while letting it scale



#current = head
#while current:
 #   current = current.next 

#I am creating the key
#never mind I am creating the set 
        seen = set()

        for v in nums:         #for loop
            if v in seen:       #if v(the value) is in seen(the set) that mean there is a duplicate if there is not it will be added in the set then returns false
                return True
            seen.add(v)  #add to the set
        return False       
    






