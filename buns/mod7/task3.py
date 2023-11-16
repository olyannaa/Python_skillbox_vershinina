import time
import functools

# Декоратор timer
def timer(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"The function {func.__name__} took {end_time - start_time} seconds to execute")
    return result
  return wrapper

# Декоратор memoize
def memoize(func):
  cache = {}

  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    if args not in cache:
      cache[args] = func(*args, **kwargs)
    return cache[args]

  return wrapper

# Декоратор validate_args
def validate_args(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    if len(args) != 1:
      return "Not enough arguments" if len(args) < 1 else "Too many arguments"
    elif not isinstance(args[0], int):
      return "Wrong types"
    elif args[0] < 0:
      return "Negative argument"
    return func(*args, **kwargs)

  return wrapper

# Применение всех трех декораторов к функции fibonacci
@timer
@memoize
@validate_args
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Сравнение скорости выполнения функции Fibonacci с и без декоратора memoize
print("Execution time without memoization:")
fibonacci(35)

# Очистка кэша для функции fibonacci
fibonacci.__wrapped__.__wrapped__.__dict__.clear()

print("\nExecution time with memoization:")
fibonacci(35)
