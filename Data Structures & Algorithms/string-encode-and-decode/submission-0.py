class Solution:

    def encode(self, strs: List[str]) -> str:
    #this is not a count or a set so i dont know what pattern

    #im thinking find the length of the string, put it in a list, then append after that lenght number a hashtag then i add the string, then i continue\
        res = []
        for word in strs:
            res.append(str(len(word)) + "#")
            res.append(word)
        return "".join(res)
    def decode(self, s: str) -> List[str]:




 
    #for the decoder i want an empty list and i want to loop through the elements of the entire res list. I have to slice to get the seperate strings
        decoder = []
        i = 0 # how do i slice the correct strings is my question
        while i < len(s):
            j = i #i want it to keep walking foward until it hits a hashtag
            while s[j] != "#":
                j +=1
            length = int(s[i:j])
            word = s[j + 1: j + 1 + length]
            decoder.append(word)
            i = j + 1 + length
        return decoder



            
