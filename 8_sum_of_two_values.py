def sum_of_two(n, x, nums):
    numsDict = {}

    for i in range(n):
        y = x - nums[i]
        if y in numsDict:
            return numsDict[y] + 1, i + 1
        
        numsDict[nums[i]] = i
    return "IMPOSSIBLE"

n, x = map(int, input().split())
nums = list(map(int, input().split()))

result = sum_of_two(n, x, nums)

if result == "IMPOSSIBLE":
    print(result)
else:
    print(result[0], result[1])