
#task11
def check_winner(board):
  size = len(board)

  for row in board:
    if row.count("X") == size: return "X"
    elif row.count("O") == size: return "O"

  for col in range(size):
    column = [board[row][col] for row in range(size)]
    if column.count("X") == size:return "X"
    elif column.count("O") == size:return "O"

  diagonal1 = [board[i][i] for i in range(size)]
  diagonal2 = [board[i][size-i-1] for i in range(size)]
  if diagonal1.count("X") == size or diagonal2.count("X") == size: return "X"
  elif diagonal1.count("O") == size or diagonal2.count("O") == size: return "O"

  return "Ничья"

board = [["_", "X", "O"],
["X", "O", "O"],
["O", "O", "_"]]
print(check_winner(board))