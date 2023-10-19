#task5
name = '123.txt'
f = open(name, 'r')
a = f.readline()
result =[]
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(26):
  result.append([alphabet[i], a.count(alphabet[i])])
result.sort(key = lambda x: x[1], reverse=True)
print(result)