class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n

        while low <= high:
            mid = (low + high) // 2
            result = guess(mid)

            if result == 0:
                return mid
            
            if result < 0:
                high = mid - 1
            else:
                low = mid + 1
                
        return -1