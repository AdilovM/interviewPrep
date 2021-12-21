def mod_power_2(x, power)->int:
  return x & ((1 << power) - 1)
#print(mod_power_2(77,6))