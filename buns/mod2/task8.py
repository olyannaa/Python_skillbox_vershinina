#task8
def counter(s, i):
  k= 0
  for s_s in s:
    if s_s == i:
      k+=1
    else:
      break
  return k
s, i = str(input()).split(",")
print(counter(s, i))

