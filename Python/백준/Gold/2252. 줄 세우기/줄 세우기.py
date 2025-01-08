import sys

N, M = map(int, sys.stdin.readline().split())

inDegrees = [0] * N
outDegrees = [set() for _ in range(N)]
zeroInDegrees = set()

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())

    a -= 1
    b -= 1
    
    inDegrees[b] += 1
    outDegrees[a].add(b)

for i, inDegree in enumerate(inDegrees):
    if not inDegree: zeroInDegrees.add(i)

answer = []
for i in range(N):
    # 진입 차수가 0 인 애들 중에 하나 뽑기
    prob = zeroInDegrees.pop()
    
    # 사용한 노드 목록에 추가
    answer.append(str(prob + 1))
    
    # 걔 이후로 연결된 노드들의 진입차수 -1
    # 하면서 동시에 0인지 체크해서 zeroIndegrees 에 넣기
    for out in outDegrees[prob]:
        inDegrees[out] -= 1
        if inDegrees[out] == 0: zeroInDegrees.add(out)

print(' '.join(answer))