import random
a = input('Maxium: ')
b = input('Minmum: ')
a = int(a)
b = int(b)
rn = random.randint(a, b)
c = 0
while True:
    n = input('Please guess the number: ')
    n = int(n)
    c = c + 1
    if n == rn:
      print('Right.')
      print('You have already guessd', c ,'times')
      break
    elif n > rn:
      print('Again. Smaller.')
    elif n < rn:
      print('Again, Bigger.')
    print('You have already guessd', c ,'times')