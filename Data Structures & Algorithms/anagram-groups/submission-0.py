class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #so i need to group anagrams together
        #breaking it down I need the strings into characters
        #then i use that character and match it with the rest

        #using a set I could do that

        #question is how do I add it into groups aka creating a new group for each one 

        group = {}


        for word in strs:
            #how do i add each one and compare
            key = "".join(sorted(word))
            if key not in group:
                group[key] = []

            group[key].append(word)
        return list(group.values())