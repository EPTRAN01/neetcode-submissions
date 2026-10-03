class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Get the string
        #get it where the number of characters appear the same number of time s
        # I am suspecting hashtable again

       # hashset = set()
       # for n in s:
     #       hashset.add(s)



     #   hashset2 = set()
      #  for n in t:
       #     hashset2.add(s)


         #  if hashset == hashset2:
        #       return True:
         #   else:
         #       return False:


         #       nvm its hashmap this logic i did seems flawed due to me needing the actual character and count

      counter_s = {}
      for char in s:
        #counter
        if char not in counter_s:
          #i want it to add the the dict and count it
          counter_s[char] = 1 #if it is the first time seeing it set the count to 1
        else:
          counter_s[char] += 1 #otherwise if its in it already add 1 to the count
      counter_t = {}
      for char in t:
          if char not in counter_t:
            counter_t[char] = 1
          else:
            counter_t[char] += 1
      #compare counter values
      if counter_s == counter_t:
        return True
      else:
        return False
