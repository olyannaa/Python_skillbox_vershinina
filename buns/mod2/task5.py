#task5
def shift_character(i, n):
  alpha = 'abcdefghijklmnopqrstuvwxyz'
  n = int(n)
  x = alpha.index(i) # searhing the index of a character in the alphabet
  shifted_x = (x + n) % len(alpha) # calculating the index of a new character

  k = alpha[shifted_x]

  return k

i, n = str(input()).split(",")
print(shift_character(i, n))

