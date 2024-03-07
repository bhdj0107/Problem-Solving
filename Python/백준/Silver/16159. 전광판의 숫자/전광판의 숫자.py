# 2021 07 07 2216 start
import sys
panel = ["" for _ in range(7)]

# 숫자와 전광판 대치 딕셔너리
num = {}
num[0] = ["000000","001100","010010","010010","010010","001100","000000"]

num[1] = ["000000","000100","001100","000100","000100","000100","000000"]

num[2] = ["000000","011110","000010","011110","010000","011110","000000"]

num[3] = ["000000","011100","000010","000100","000010","011100","000000"]

num[4] = ["000000","000100","001100","010100","111110","000100","000000"]

num[5] = ["000000","011110","010000","011100","000010","010010","001100"]

num[6] = ["000000","010000","010000","011110","010010","011110","000000"]

num[7] = ["000000","011110","000010","000100","000100","000100","000000"]

num[8] = ["000000","011110","010010","011110","010010","011110",'000000']

num[9] = ["011110","010010","010010","011110","000010","000010","000010"]

tmp = list(num.keys())
for i in tmp:
    num[tuple(num[i])] = i

data = []
numbers = []
num_cnt = {i:0 for i in range(10)}
for i in range(7): data.append(sys.stdin.readline().rstrip())
N = len(data[0]) // 6

# 등장하는 숫자를 순서대로 배열에 저장하고
# 숫자의 갯수를 세어놓는다

for i in range(N):
    inp = []
    for j in range(7):
        inp.append(data[j][i * 6:i * 6 + 6])
    tmp = num[tuple(inp)]
    numbers.append(tmp)
    num_cnt[tmp] += 1
	
# 등장횟수가 0인 숫자는 삭제한다
for i in list(num_cnt.keys()):
	if num_cnt[i] == 0: del num_cnt[i]

# 다음 사전순 글자를 찾는 방법
swp_num = 0
for i in range(len(numbers) - 1, 0, -1):
	if numbers[i] > numbers[i - 1]:
		swp_num = i
		break


if swp_num == 0: print("The End")
else:
	for i in range(0, swp_num - 1):
		num_cnt[numbers[i]] -= 1
		if num_cnt[numbers[i]] == 0: del num_cnt[numbers[i]]
	# 먼저 스왑넘 전칸을 다음 큰 숫자로 바꾼다.
	for i in range(numbers[swp_num - 1] + 1, 10):
		if i in num_cnt:
			numbers[swp_num - 1] = i
			num_cnt[i] -= 1
			if num_cnt[i] == 0: del num_cnt[i]
			break
	# 숫자가 바뀐 칸 뒤로는 작은 숫자들을 순서대로 붙여넣으면 된다.
	# 이때, 카운트가 0인 숫자는 모두 기존에 삭제하였으므로,
	# 즉, 뒤에 올 수 있는 숫자들만 카운트 딕셔너리에 저장되어있으므로,
	# 카운트에 등록된 숫자중 가장 작은 수를 배열에 더하고 카운트를 하나 내린다
	# 마찬가지로 0이된 카운트는 삭제한다.
	for i in range(swp_num, N):
		tmp = min(num_cnt.keys())
		numbers[i] = tmp
		num_cnt[tmp] -= 1
		if num_cnt[tmp] == 0: del num_cnt[tmp]

	# 출력
	for i in numbers:
		for j in range(7):
			panel[j] += num[i][j]
	for i in panel:
		print(i)