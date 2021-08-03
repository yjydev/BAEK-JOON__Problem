T = int(input())
result = []
list_1 = sorted(list(map(int, input().split(" "))))

for i in T:
    result.append(sum(list_1[0:i+1]))
print(sum(result))
