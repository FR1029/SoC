n, m, k = map(int, input().split())
desired = list(map(int, input().split()))
apartment = list(map(int, input().split()))
i = j = count = 0

desired.sort()
apartment.sort()

while i < n and j < m:
    if apartment[j] < desired[i] - k:
        j += 1
    elif apartment[j] > desired[i] + k:
        i += 1
    else:
        count += 1
        i += 1
        j += 1

print(count)
