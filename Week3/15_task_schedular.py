from typing import Counter, List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = list(Counter(tasks).values())
        max_freq = max(freq)
        max_count = freq.count(max_freq)
        part_count = max_freq - 1
        part_length = n + 1
        empty_slots = part_count * part_length + max_count

        return max(len(tasks), empty_slots)