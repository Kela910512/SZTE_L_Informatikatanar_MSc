n = int(input())
nums = list(map(int, input().split()))

totSum = n * (n + 1) // 2

tmpSum = sum(nums)

result = totSum - tmpSum

print(result)