def validate_args(func):
  def wrapper(*args):
    if len(args) != 1:
      return "Not enough arguments" if len(args) < 1 else "Too many arguments"
    elif not isinstance(args[0], int):
      return "Wrong types"
    elif args[0] < 0:
      return "Negative argument"
    return func(*args)
  return wrapper

@validate_args
def example_function(num):
  return f"The argument is {num}"

# Примеры использования
print(example_function(5)) # Вывод: "The argument is 5"
print(example_function(-2)) # Вывод: "Negative argument"
print(example_function(3, 7)) # Вывод: "Too many arguments"
print(example_function("test")) # Вывод: "Wrong types"
