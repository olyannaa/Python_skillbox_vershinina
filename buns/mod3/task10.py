#task10
size = int(input())
m = []
for i in range(size): m.append(i+1)
m = [m] * size
print(m)
trans_m = [[m[j][i] for j in range(size)] for i in range(size)]
print(trans_m)
