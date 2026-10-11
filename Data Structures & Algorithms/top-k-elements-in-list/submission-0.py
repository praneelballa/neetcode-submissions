class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

            hashmap={}

            for i in nums:
                hashmap[i]=hashmap.get(i, 0 )+1

            top_nums= sorted(
                hashmap,
                key=lambda num: hashmap[num],
                reverse=True
            )
            return top_nums[:k]