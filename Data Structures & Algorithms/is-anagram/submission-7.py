class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #the problem is asking anagram which mean if they have the same amount of letters then they return true otherwise return false
        #right away i can cancel out any case if they dont have the same amount which i can do through len
        if len(s) != len(t):
            return False


        #so what is the pattern for this?
        #im going through existing values and comparing it
        #so i could do a hashmap
        #a frequency map

        countS, countT = {}, {}
        #okay I initialize the dictioanry for both s and t

        for c in range(len(s)):
           countS[s[c]] = 1 + countS.get(s[c], 0)
           countT[t[c]] = 1 + countT.get(t[c], 0)
        return countS == countT
        #get the range of s[c] since it is the same length. Then I make it add 1 to the count if not its zero. Then if it is not there for the index I use the .get function to find it

        #The return to see if it is true