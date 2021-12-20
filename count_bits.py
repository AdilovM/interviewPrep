def count_bits(x: int) -> int:
  num_bits = 0
  while x:
    # num_bits += x & 1
    # x >> 1
    num_bits += 1
    x &= x - 1 # reducing time complexity by erasing lowest set bit -
  return num_bits



