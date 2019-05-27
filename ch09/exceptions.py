try:
  typo
except Exception as err:
  print(err)

try:
  a = 4 / 0
except Exception as err:
  print(err)
