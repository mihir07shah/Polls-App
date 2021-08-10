def my_func(st):
  l1 = [ch for ch in st if ch.isalpha()]
  return ''.join(l1.pop() if ch.isalpha() else ch for ch in st)


st = 'ab-cd-ef'
print(my_func(st))