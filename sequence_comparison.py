# longest commun sequence

# a memoized recursive solution to the LCS problem
def rec_lcs(a,b):
  memo  # L ismemoized
  def L(i,j):   # prefixes a[:i] and b[:j]
    if min(i,j)<0:return 0  # one prefix is empty
    if a[i] == b[j]: return 1+L(i-1,j-1)  # match, move diagonally
    return max(L(i-1,j),L(i,j-1)) # chop off either a[i] or b[j]
  return L(len(a)-1,len(b)-1) # run L on entire sequences

# a version that saves memory by only  keeping the current and the previous row of the DP matrix
def lcs(a,b):
  n,m = len(a),len(b)
  pre, cur = [0]*(n+1),[0]*(n+1)  # previous/current row
  for j in range(i,m+1):          # iterative over b
    pre,cur=cur,pre               # keep prev., overwrite cur.
    for i in range(1,n+1):        # iterate over a
      if a[i-1]==b[j-1]:          # last elts. of pref. equal ?
        cur[i]=pre[i-1]+1         # L(i,j) = L(i-1,j-1) + 1
      else:                   
        cur[i]=max(pre[i],cur[i-1]) # max(L(i,j-1), L(i-1,j))
  return cur[n]                     # L(n,m)

