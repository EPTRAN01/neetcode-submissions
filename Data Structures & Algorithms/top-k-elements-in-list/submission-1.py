class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #i see the pattern where i have to keep a count so a hashmap

        for i in nums:
            count[i] = count.get(i, 0) + 1

        

        #now it gave me a value and index

        # i see the pattern where this will need a bucket since i want the highest one

      
         # i also see i need to create a frequency
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
                bucket[freq].append(num)

        res = []
        for i in range(len(bucket) -1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res