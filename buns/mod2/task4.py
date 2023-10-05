#task4
def binar(n):
  b = ''
  while n > 0:
    b = str(n % 2) + b
    n = n // 2
  return b
def octa(n):
  o = ''
  while n > 0:
    o = str(n % 8) + o
    n = n // 8
  return o
def hexa(n):
  s = ''
  h = '0123456789ABCDEF'
  while n > 0:
    s = h[n % 16] + s
    n = n // 16
  return s

n = int(input())
print("{}, {}, {}".format(binar(n), octa(n), hexa(n)))

print(bin(n), oct(n), hex(n))

