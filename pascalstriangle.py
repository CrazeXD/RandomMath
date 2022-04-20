def generate_triangle(exponent, triangle=[]):
  for row in range(exponent+1):
    currentrow = []
    currentrow.append(1)
    if row == 0:
      pass
    elif row == 1:
      currentrow.append(1)
    else:
      prevrow = triangle[row-1]
      count = 0
      for j in prevrow:
        count+=1
      for i in range(1, count):
        val = triangle[row-1][i-1]+triangle[row-1][i]
        currentrow.append(val)
      currentrow.append(1)
    triangle.append(currentrow)
  return triangle