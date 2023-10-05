
#task11
string = str(input()).split()
k = False
for i in string:
  if string.count(i)>1:
    k = True
    break
print(k)

