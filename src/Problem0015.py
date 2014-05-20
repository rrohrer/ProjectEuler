hit_counter = 0

def n_n_solve(x, y, width, height):
  if x <= width:
    n_n_solve(x + 1, y, width, height)
  if y <= height:
    n_n_solve(x, y + 1, width, height)
  if x == width and y == height:
    global hit_counter
    hit_counter += 1

n_n_solve(0, 0, 20, 20)
print hit_counter
