import sys
#import tester
inp = []
for line in sys.stdin:
	inp.append(line.rstrip())
#for line in tester.f.readlines():
#	inp.append(line.rstrip())
for i in range(len(inp) // 32):
	Mem = []
	for j in range(32):
		Mem.append(inp[32 * i + j])
	counter, adder = 0, 0
	while True:
		op, target = Mem[counter][:3], int(Mem[counter][-5:],2)
		counter += 1
		counter %= 32
		if op == "000":
			value = "{:0>8}".format(format(adder,'b'))
			Mem[target] = value
		elif op == "001":
			adder = int(Mem[target], 2)
		elif op == "010":
			if adder == 0:
				counter = target
		elif op == "100":
			adder -= 1
			adder = adder % 256
		elif op == "101":
			adder += 1
			adder = adder % 256
		elif op == "110":
			counter = target
		elif op == "111":
			break
	print("{:0>8}".format(format(adder,'b')))