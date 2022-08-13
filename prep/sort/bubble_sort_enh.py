# Bubble Sort (Enhanced)

import unsorted
import time
import sort_visualizer as vis
from random import shuffle

def main(list):
  count = len(list)
  end = count - 1
  while end > 0:
    last = 1
    for i in range(end):
      vis.bubble(list, 0, i, end+1, count)
      vis.compare(list, i, i+1)
      if list[i] > list[i+1]:
        vis.swap(list, i, i+1)
        list[i], list[i+1] = list[i+1], list[i]
        last = i + 1
    end = last - 1
  vis.bubble(list, 0, None, 0, count)

  # print(list) 



if __name__ == '__main__':
  list = unsorted.numbers[:25]

  vis.init('Bubble Sort Enhanced')
  # shuffle(list)
  vis.setup(list)
  vis.speed = 100

  started = time.time()
  main(list)
  elapsed = time.time() - started
  print('Elapsed: %.4fs' % elapsed)
  vis.end()
