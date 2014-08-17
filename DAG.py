# overlapping subproblems: finding the distance b-f requires finding the shortest path, for ex, d-f.
# the magic of memoization removes all the redundancy, and we end up with a linear time algorithm

def rec_dag_sp(W,s,t): # shortest path from s to t
  @memo # memoize f
  def d(u):
    if u==t:return 0
    return min(W[u][v]+d(v) for v in W[u])
  return d(s)
  
# the iterative version of DAG works by propagating partial solutions step by step, using the relaxation idea

def dag_sp(W,s,t):
  d ={u:float('inf') for u in W}
  d[s] = 0
  for u in topsort(W):
    if u==t: break
    for v in W[u]:
      d[v] = min(d[v],d[u]+W[u][v])
  return d[t]
