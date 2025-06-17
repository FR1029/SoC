from typing import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        sorted_items = list(sorted(freq.items(), key=lambda x: x[1], reverse=True))
        result = ''.join(char*freq for char, freq in sorted_items)

        return result