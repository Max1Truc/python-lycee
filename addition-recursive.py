def add(a,b):
  c, d = a ^ b, (a & b) * 2

  if c ^ d != c | d:
    return add(c, d)
  else:
    return c | d

if __name__ == "__main__":
  a = int(input("a ? "))
  b = int(input("b ? "))
  print("a + b =", add(a, b))
