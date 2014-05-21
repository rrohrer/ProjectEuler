hit_counter = 0

def n_n_solve(x, y, width, height):
  if x <= width:
    n_n_solve(x + 1, y, width, height)
  if y <= height:
    n_n_solve(x, y + 1, width, height)
  if x == width and y == height:
    global hit_counter
    hit_counter += 1

#n_n_solve(0, 0, 20, 20)
#print hit_counter


def dynamic_progaming_solve(w, h):
  width = w + 1
  height = h + 1
  grid = [1] * width * height
  for x in range(1, width):
    for y in range(1, height):
      grid[width * y + x] = grid[width * y + (x - 1)] + grid[width * (y - 1) + x]
  return grid[-1]

print dynamic_progaming_solve(20, 20)
