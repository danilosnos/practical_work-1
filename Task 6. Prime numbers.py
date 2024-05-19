def sieve_of_eratosthenes(limit):
  """
  Находит все простые числа до заданного предела, используя метод «Решето Эратосфена».

  Args:
    limit: Максимальное число.

  Returns:
    Список простых чисел.
  """
  primes = [True] * (limit + 1)
  primes[0] = primes[1] = False

  for i in range(2, int(limit*0.5) + 1):
    if primes[i]:
      for j in range(i * i, limit + 1, i):
        primes[j] = False

  return [i for i in range(limit + 1) if primes[i]]

def print_primes_by_decade(primes):
  """
  Выводит простые числа, группируя их по десяткам.

  Args:
    primes: Список простых чисел.
  """
  print("Простые числа:")
  decade_start = -1
  current_decade = []
  for prime in primes:
    if prime // 10 != decade_start:
      if current_decade:
        print(", ".join(map(str, current_decade)))
      decade_start = prime // 10
      current_decade = [prime]
    else:
      current_decade.append(prime)
  if current_decade:
    print(", ".join(map(str, current_decade)))

if __name__ == "__main__":
  try:
    max_number = int(input("Введите максимальное число (не более 1000): "))
    if max_number > 1000:
      raise ValueError
  except ValueError:
    print("Ошибка: Введите целое число, не превышающее 1000.")
  else:
    primes = sieve_of_eratosthenes(max_number)
    print_primes_by_decade(primes)