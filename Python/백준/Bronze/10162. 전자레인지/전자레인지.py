T = int(input())
if T % 10:
    print(-1)
    exit()

print(T // 300, end=" ")
T = T % 300
print(T // 60, end=" ")
T = T % 60
print(T // 10)
