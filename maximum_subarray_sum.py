n = int(input())
arr = list(map(int, input().split()))
max_current = maximum = arr[0]

for i in range(1, n):
    max_current = max(arr[i], max_current + arr[i])
    maximum = max(maximum, max_current)

print(maximum)