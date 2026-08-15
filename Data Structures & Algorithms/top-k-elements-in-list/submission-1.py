class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}
        for i in nums:
            if i in hash_table:
                hash_table[i] += 1
            else:
                hash_table[i] = 1
        hash_table = dict(sorted(hash_table.items(), key=lambda item: item[1], reverse=True))
        return list(hash_table)[:k]

        