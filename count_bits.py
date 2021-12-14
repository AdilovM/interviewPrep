def count_bits(x: int) -> int:
  num_bits = 0
  while x:
    num_bits += x & 1 #checks if the rightmost bit is 1 (0001 & 0001 = 1)
    x >> 1 # return x after dropping right bit (1) of binary 7. '{0:08b}'.format(9) is 000001001 and {0:08b}'.format(9 >> 1) is 000000100
  return num_bits
