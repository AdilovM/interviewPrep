def parity(x:int)->int:
  result = 0
  while x:
    # result ^= x & 1
    # x >>= 1
    result ^= 1
    x & x - 1
  return result
