import sys

dic = {}

dic["`"] = 0
dic["1"] = 0
dic["Q"] = 0
dic["A"] = 0
dic["Z"] = 0

dic["2"] = 1
dic["W"] = 1
dic["S"] = 1
dic["X"] = 1

dic["3"] = 2
dic["E"] = 2
dic["D"] = 2
dic["C"] = 2

dic["4"] = 3
dic["5"] = 3
dic["R"] = 3
dic["T"] = 3
dic["F"] = 3
dic["G"] = 3
dic["V"] = 3
dic["B"] = 3

dic["6"] = 4
dic["7"] = 4
dic["Y"] = 4
dic["U"] = 4
dic["H"] = 4
dic["J"] = 4
dic["N"] = 4
dic["M"] = 4

dic["8"] = 5
dic["I"] = 5
dic["K"] = 5
dic[","] = 5

dic["9"] = 6
dic["O"] = 6
dic["L"] = 6
dic["."] = 6

dic["0"] = 7
dic["-"] = 7
dic["="] = 7
dic["P"] = 7
dic["["] = 7
dic["]"] = 7
dic[";"] = 7
dic["'"] = 7
dic["/"] = 7




count = [0 for _ in range(8)]
inp = sys.stdin.readline().rstrip()
for i in inp:
    count[dic[i]] += 1
for i in count:
    print(i)