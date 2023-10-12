
#task9
def spiral_position(N):
  x = 0 
  y = 0 
  direction = 0
  steps = 1 
  count = 0 

  while count < N:
    for _ in range(2):
      for _ in range(steps):
        if direction == 0:
          x -= 1
        elif direction == 1:
          y -= 1
        elif direction == 2:
          x += 1
        else:
          y += 1
        count += 1
      if count == N:
        return x, y
    direction = (direction + 1) % 4
  steps += 1

  return x, y

N = int(input())
position = spiral_position(N)
print(position[0], position[1])

