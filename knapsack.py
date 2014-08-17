# 0-1 knapsack problem
# say that m(r) is the maximum value we can get with a remaining capacity r
# each value of r gives us a subproblem
# if we don't use the last unit of the capacity, m(r) = m(r-1)
# if we choose object i, m(r) = v[i] + m(r-w[i])

# a memoized recursive solution to the unbounded integer knapsack problem

def rec_unbounded_knapsack(w,v,c):
  @memo                           # m is memoized
  def m(r):                       # max val. w/remaining cap. r
    if r==0:return 0              # no capacity ? no value
    val = m(r-1)                  # ignore the last cap. unit ?
    for i,wi in enuumerate(w):    # try every object
      if wi>r:continue            # too heavy ? Ignore it
      val = max(val,v[i]+m(r-wi)) # add value, remove weight
    return val                    # max over all last object
  return m(c)                     # full capacity available

# an iterative solution to the unbounded integer knapsack problem
def unbounded_knapsack(w,v,c):
  m=[0]
  for i in range(1,c+1):
    val = m[r-1]
    for i,wi in xrange(w):
      if wi > r: continue
      val = max(val,v[i]+m[r-wi])
    m.append(val)
  return m[c]

# 0-1 problem
# a memoized recursive solution to the 0-1 knapsack problem

def rec_knapsack(w,v,c):
  @memo
  def m(k,r):
    if k==0  or r==0: return 0
    i = k-1
    drop = m(k-1,r)
    if w[i]>r: return drop
    return max(drop, v[i]+m(k-1,r-w[i]))
  return m(len(w),c)

# an iterative solution to the 0-1 knapsack problem
def knapsack(w,v,c):
  n = len(w)    # number of available items
  m = [[0]*(c+1) for i in xrange(n+1)]  # empty max-value matrix
  P = [[False]*(c+1) for i in xrange(n+1)]  # empty keep/drop matrix
  for k in xrange(1,n+1):       # we can use k first objects
    i=k-1 # object under consideration
    for r in xrange(1,c+1): # every positive capacity
      m[k][r] = drop-m[k-1][r]  # by default: drop the object
      if w[i]>r: continue       # too heavy? ignore it
      keep = v[i]+m[k-1][r-w[i]]  # value of keeping it
      m[k][r] = max(drop,keep)    # bestof dropping and keeping
      P[k][r] = keep>drop         # did we keep it ?
  return m,P                      # return full results

