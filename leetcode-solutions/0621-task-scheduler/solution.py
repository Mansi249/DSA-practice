from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        maxFreq = max(count.values())

        countMax = 0
        for freq in count.values():
            if freq == maxFreq:
                countMax += 1

        return max(len(tasks), (maxFreq - 1) * (n + 1) + countMax)
