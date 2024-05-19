def get_fib_numbers(qty):
  """
  Возвращает список чисел Фибоначчи заданной длины.

  Args:
    qty: Количество чисел Фибоначчи для генерации.

  Returns:
    Список чисел Фибоначчи.
  """
  fib_numbers = []
  a = 0
  b = 1
  for _ in range(qty):
    fib_numbers.append(a)
    a, b = b, a + b
  return fib_numbers

fib_numbers = get_fib_numbers(10)
assert len(fib_numbers) == 10
print(fib_numbers)