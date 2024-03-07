import sys
Wo, Ao, T = map(int, sys.stdin.readline().split())
D, I, As = map(int, sys.stdin.readline().split())

def simulation_no_change():
  W = Wo
  for _ in range(D):
    W -= (Ao + As - I)
    if W <= 0:
      print("Danger Diet")
      return

  print(W, Ao)

def simulation_change():
  W = Wo
  A = Ao

  for _ in range(D):
    W -= (A + As - I)
    if W <= 0:
      print("Danger Diet")
      return

    if abs(A + As - I) > T:
      A = A + (I - A - As) // 2
      if A <= 0:
        print("Danger Diet")
        return

  if Ao > A:
    print(W, A,"YOYO")
  else:
    print(W, A, "NO")
    
simulation_no_change()
simulation_change()