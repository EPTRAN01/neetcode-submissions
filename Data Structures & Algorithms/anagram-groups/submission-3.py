from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #it ask to group the anagrams together
        # but if it does not have one it gets put into a seperate group

        #pattern? Well im thinking of a key and that keyis going to be  count in it then it groups it


        #count = {[26]*0 }
        #i get the count that has every count for every letter and if it is not there it is 0

       # for loop through the str
       # then loop again to get the char in that str
       # then count 
       # if it is already seen in the key then add to it
       # if not then initalize its own group
      # key = {}
      #  for n in strs:
         #   for c in n:
                #get the counter

        res = defaultdict(list)

        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c) - ord('a')] += 1
            res[(tuple(count))].append(word)
        return list(res.values())