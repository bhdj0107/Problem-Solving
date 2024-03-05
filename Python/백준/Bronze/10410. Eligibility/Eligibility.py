import sys
N = int(sys.stdin.readline())
for _ in range(N):
    name, ps, birth, course = sys.stdin.readline().split()
    psY = ps.split('/')[0]
    birthY = birth.split('/')[0]
    if int(psY) >= 2010 or int(birthY) >= 1991:
        print(name + " eligible")
    elif int(course) > 40:
        print(name + " ineligible")
    else:
        print(name + " coach petitions")