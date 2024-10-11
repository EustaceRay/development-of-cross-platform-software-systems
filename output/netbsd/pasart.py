def print_centered(text, width):
  """Prints text centered within a specified width."""
  padding = (width - len(text)) // 2
  print(" " * padding + text)

print_centered("PASART", 24)
print_centered("CREATIVE COMPUTING", 18)
print_centered("MORRISTOWN NEW JERSEY", 16)
print()
print()
print()

p = [[0 for _ in range(36)] for _ in range(36)]

print("THIS PROGRAM CREATES ARTIST DESIGNS BASED ON PASCAL'S TRIANGLE.")
print("YOU HAVE 3 BASIC TYPES OF DESIGNS TO SELECT FROM:")
print("1. A SINGLE PASCAL'S TRIANGLE (PLAYED WITH AN ARTISTIC FLARE)")
print("2. TWO 'ARTSY' PASCAL'S TRIANGLES PRINTED BACK TO BACK")
print("3. FOUR 'ARTSY' TRIANGLES IN THE CORNER OF A SQUARE ARRAY.")

while True:
  option = input("WHAT'S YOUR PLEASURE? 1, 2 OR 3: ")
  if option in ('1', '2', '3'):
    break
  else:
    print("Invalid input. Please enter 1, 2 or 3.")

while True:
  blanks = input("WHICH MULTIPLES DO YOU WANT REPRESENTED WITH BLANKS: ")
  try:
    blanks = int(blanks)
    break
  except ValueError:
    print("Invalid input. Please enter an integer.")

while True:
  size = input("HOW MANY ROWS AND COLUMS IN THE ARRAY (36 IS MAXIMUM): ")
  try:
    size = int(size)
    if 0 < size <= 36:
      break
    else:
      print("Invalid input. Please enter an integer between 1 and 36.")
  except ValueError:
    print("Invalid input. Please enter an integer.")

if option == '1':
  for r in range(size):
    for c in range(size):
      if r == 0 or c == 0:
        p[r][c] = 1
      else:
        p[r][c] = p[r][c - 1] + p[r - 1][c]

  for r in range(size):
    for c in range(size):
      if p[r][c] % blanks == 0:
        print(" ", end=" ")
      else:
        print("* ", end=" ")
    print()

elif option == '2':
  n = size
  z = size

  for r in range(n):
    for c in range(z - 1):
      if r == 0 or c == 0:
        p[r][c] = 1
      else:
        p[r][c] = p[r][c - 1] + p[r - 1][c]
    z -= 1

  z = n
  n = 2
  for r in range(z, 0, -1):
    for c in range(z, n, -1):
      if r == z or c == z:
        p[r][c] = 1
      else:
        p[r][c] = p[r][c + 1] + p[r + 1][c]
    n += 1

  for r in range(size):
    for c in range(size):
      if p[r][c] % blanks == 0:
        print(" ", end=" ")
      else:
        print("* ", end=" ")
    print()

elif option == '3':
  y = size
  z = size // 2
  z1 = z
  z2 = z
  z3 = z
  x4 = z
  x5 = x4

  for i in range(z1):
    for j in range(z):
      if i == 0 or j == 0:
        p[i][j] = 1
      else:
        p[i][j] = p[i][j - 1] + p[i - 1][j]
    z -= 1

  for i in range(z1):
    for j in range(y, x5 + 1, -1):
      if i == 0 or j == y:
        p[i][j] = 1
      else:
        p[i][j] = p[i][j + 1] + p[i - 1][j]
    x5 += 1

  for i in range(y, x4 + 1, -1):
    for j in range(z2):
      if i == y or j == 0:
        p[i][j] = 1
      else:
        p[i][j] = p[i][j - 1] + p[i + 1][j]
    z2 -= 1

  for i in range(y, n + 1, -1):
    for j in range(y, z3 + 1, -1):
      if i == y or j == y:
        p[i][j] = 1
      else:
        p[i][j] = p[i + 1][j] + p[i][j + 1]
    z3 += 1

  for r in range(size):
    for c in range(size):
      if p[r][c] % blanks == 0:
        print(" ", end=" ")
      else:
        print("* ", end=" ")
    print()