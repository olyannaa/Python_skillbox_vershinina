#task2
def power(a, n):
  if n%2 == 0: return (a**2)**(n/2)
  elif n%2 == 1: return a * (a**(n-1))

