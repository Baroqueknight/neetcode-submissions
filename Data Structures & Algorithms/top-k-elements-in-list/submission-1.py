class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1  # Cleaner way to count frequencies
            
        # Sort the dictionary items (tuples of key, value) by frequency (x[1]) in reverse
        sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)
        
        # Extract just the keys of the top k items
        return [item[0] for item in sorted_items[:k]]
            