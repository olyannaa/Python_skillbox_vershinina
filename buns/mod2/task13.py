
#task13
def correct(n):
  even = 0
  odd = 0
  for i in n:
    if n.index(i)%2!=0:even += int(i)
    elif n.index(i)%2==0: odd += int(i)
  if (even*3 + odd)%10 == 0: return "yes"
  elif (even*3 + odd)%10 != 0: return "no"

bar_code = str(input())
correct(bar_code)