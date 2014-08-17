# Fibonacci 

# easily implemented as a Python function
def fib(i):
  if i<2: return 1
  return fib(i-1) + fib(i-2)

# a memoizing decorator
from functools import wraps
def memo(func):
  cache = {}
  wraps(func)
  def wrap(*args):
    if args not in cache:
      cache[args] =func(*args) # compute and cache the solution
    return cache[args]
  return wrap

# the idea of a memoized function is that it caches its return value
# fib =  memo(fib)
# fib(100)

# tangled dependencies = overlapping subproblems

# Pascal triangle:
def C(n,k):
  if k==0: return 1
  if n==0: return 0
  return C(n-1,k-1) + C(n-1,k)

# using defaultdict as the cache
from collections import defaultdict
n,k = 10,7
C = defaultdict(int)
for row in range(n+1):
  C[row,0]=1
  for col in range(1,k+1):
    C[row,col] = C[row-1,col-1] + C[row-1,col]
C[n,k] # 120

# with the memoized function, we needn't worry about either issue: it will compute whatever it needs recursively.
