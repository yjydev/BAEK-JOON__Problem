# 내장함수 사용
import sys
K = int(input())
k = [int(sys.stdin.readline()) for _ in range(K)]
nums = []
for num in k:
    if num == 0:
        nums.pop()
    else:
        nums.append(num)
print(sum(nums))

# 내장함수 x
import sys
K = int(input())
k = [int(sys.stdin.readline()) for _ in range(K)]
nums = []
for num in k:
    if num == 0:
        nums.pop()
    else:
        nums.append(num)
result = 0
for ans in nums:
    result += ans
print(result)