import sys
t_list = []

# N 입력 받기
N = int(sys.stdin.readline())

# 이후 N 개의 수들을 inp에 받아옴
inp = list(map(int, sys.stdin.readline().split()))

# inp 리스트를 역순으로 탐색
for i in range(len(inp) - 1, -1, -1):
    # 인덱스가 가장 처음부분에 도달했을 경우
    # 이는 이전 순열이 없는 경우이므로 -1 출력 후 탐색 구문 탈출
    if i == 0:
        print(-1)
        break

    # 현재 인덱스가 위치한 부분의 수를 임시 리스트에 저장
    t_list.append(inp[i])

    # 만약 인덱스를 기준으로 한칸 앞의 수가 클 경우,
    # 이전 순열을 생성한다.
    if inp[i] < inp[i - 1]:

        # 한 칸 앞의 수를 임시 변수에 저장
        temp = inp[i - 1]
        # 그 자리를 0으로 초기화 한다.
        inp[i - 1] = 0

        # 그 이후 임시 리스트에 저장된 수들 중,
        # 원래 한 칸 앞에 위치해 있던 수보다 작은 수 중에서
        # 가장 큰 수를 해당 위치에 대입
        # 그 이후 그 수는 임시 리스트에서 삭제하고,
        # 원래 앞 자리에 있었던 수를 리스트에 추가한다.
        for j in t_list:
            if temp > j > inp[i - 1]:
                inp[i - 1] = j
                del t_list[t_list.index(j)]
        t_list.append(temp)

        # 그 이후 출력한다.
        for j in range(i):
            print(inp[j], end=" ")
        while len(t_list) > 1:
            t = max(t_list)
            del t_list[t_list.index(t)]
            print(t, end=" ")
        print(t_list[0])
        break