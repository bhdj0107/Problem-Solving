import sys
inp = "@" + sys.stdin.readline().rstrip() + "#"
cnt = 0
# 크로아티아 알파벳
# č	c=
# ć	c-
# dž	dz=
# đ	d-
# lj	lj
# nj	nj
# š	s=
# ž	z=

# c 파생 : c=, c-
# d 파생 : dz=, d-
# lj, nj, s=, z=
for i in range(1, len(inp) - 1):
    temp = inp[i]
    if inp[i] == "=" or inp[i] == "-":
        if inp[i-1] in ("s", "c", "z", "d"):
            cnt += 1
    elif inp[i] == "j":
        if inp[i-1] in ("n", "l"):
            cnt += 1
    elif inp[i:i+2] == "z=":
        if inp[i-1] == "d":
            cnt += 1
print(len(inp) - cnt - 2)