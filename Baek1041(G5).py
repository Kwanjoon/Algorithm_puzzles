N = int(input())
dice = list(input().split()) #주사위에 쓰여있는 수
side = []

for t in range(len(dice)): #정수형으로 바꿔준다
  dice[t] = int(dice[t])
  
if N == 1: # 주사위가 1개인 경우
  total_1 = 0
  for d in range(len(dice)):
    total_1 += int(dice[d])
  print(total_1 - int(max(dice)))
else: # 주사위가 2개 이상인 경우
  for s in range(3):
    if dice[s] < dice[5-s]:
      side.append(dice[s])
    else:
      side.append(dice[5-s])

  side.sort()

  one = int(side[0]) * (5*N*N - 8*N + 4)
  two = int(side[1]) * (8*N - 8)
  three = int(side[2]) * 4

  total = one + two + three
  print(total)