import sys
class Node:
	def __init__(self, left=None, value=None, right=None):
		self.left, self.value, self.right = left, value, right

N=int(sys.stdin.readline())
for _ in range(N):
	inp = sys.stdin.readline().rstrip()
	head = Node()
	cur = head
	tail = Node()
	tail.left = head
	head.right = tail
	for op in inp:
		if op == '<':
			if cur != head:
				cur = cur.left
		elif op == '>':
			if cur.right != tail:
					cur = cur.right
		elif op == '-':
			if cur != head:
				cur = cur.left
				cur.right, cur.right.left = cur.right.right, cur
		else:
			tmp = Node(cur, op, cur.right)
			cur.right.left = tmp
			cur.right = tmp
			cur = tmp
	
	cur = head
	while True:
		if cur.right != tail:
			print(cur.right.value, end="")
			cur = cur.right
		else:
			break
	print()