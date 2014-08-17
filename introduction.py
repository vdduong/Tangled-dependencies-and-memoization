# have a sequence of numbers and want to find the longest increasing (non decreasing) subsequence
# ex: input [3,1,0,2,4], one solution would be [1,2,4]

# brute force algorithm (naive solution)
from itertools import combinations
def naive_lis(seq):
  for length in range(len(seq), 0,-1): # n,n-1, ... 1
    for sub in combinations(seq, length): # subsequences of given length
      if list(sub) == sorted(sub): # an increasing subsequence ?
        return sub

# a memoized recursive solution to the longest increasing subsequence problem
# focusing on the length of the solution

def rec_lis(seq):
  memo
  def L(cur):               # longest ending at seq[cur]
    res=1                   # length is at leat 1
    for pre in range(cur):  # potential predecessors
      if seq[pre]<=seq[cur]:  # a valid (smaller) predec ?
        res = max(res,1+L(pre)) # can we improve the solution ?
    return res
  return max(L(i) for i in xrange(len(seq))) # the longest of them all

# a basic iterative solution to the longest increasing subsequence problem
def basic_lis(seq):
  L= [1]*len(seq)
  for cur, val in enumerate(seq):
    for pre in range(cur):
      if seq[pre] <=val:
        L[cur]= max(L[cur], 1+L[pre])
  return max(L)

# the main time sink in the algorithm is looking over the previous elements to find the best among those that are valid 
# predecessors
# in most cases, the inner loop is devoted to a linear search that could be replaced by binary search
# a crucial point is that if more than one predec terminate subseq of length m, it doesn't matter which one of them we use
# the only safe choice would be to keep the smallest of them

from bisect import bisect
def lis(seq):
  end =[]                 # end values for all lengths
  for val in seq:         # try every value, in order
    idx = bisect(end, val)  # can we build on an end val ?
    if idx == len(end): end.append(val) # longest seq. extended
    else: end[idx] = val                # prev. endpoint reduced
  return len(end)                       # the longest we found


