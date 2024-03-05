import sys
R, C = map(int, sys.stdin.readline().split())
inp = []
for _ in range(R):
    inp.append(list(sys.stdin.readline().rstrip()))

m_count = 0
M_count = R
while m_count <= M_count:
    chk = set(zip(*inp[(M_count+m_count)//2:]))
    if len(chk) != C:
        M_count = (M_count + m_count) // 2 - 1
    else:
        m_count = (M_count + m_count) // 2 + 1
print(min(m_count, M_count))