import sys

sys.setrecursionlimit(10**8)
# quick_sort
def quick_sort(inp):
	if len(inp) <= 1:
		return inp
	left, right = [],[]
	pivot = inp.pop()
	while inp:
		tmp = inp.pop()
		if tmp < pivot:
			left.append(tmp)
		else:
			right.append(tmp)
	return quick_sort(left) + [pivot] + quick_sort(right)

N = int(sys.stdin.readline())
nums = []
for _ in range(N):
	nums.append(int(sys.stdin.readline()))
nums.sort()
for i in nums:
	print(i)