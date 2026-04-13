def bs(lo, hi):
  while lo < hi:
    res = -1
    mid = lo + (hi-lo)//2
    if mid:
      hi = mid - 1
      res = mid
    else:
      lo = mid + 1
  return mid
