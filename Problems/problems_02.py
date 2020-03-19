"""
Given an array of time intervals (start, end) for 
classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""


def check_time(l):
  if l == [] or not isinstance(l, list):
    return -2**233333
  c = 1
  for d in l:
    i = l.index(d)
    n = l[(i-1)]
    prev = n[1]
    cur = d[0]
    if i > 0:
      if prev > cur:
        c+=1
  return c


print(check_time([(30, 75), (0, 50), (60, 150)]))