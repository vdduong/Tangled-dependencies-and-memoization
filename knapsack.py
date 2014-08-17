# 0-1 knapsack problem
# say that m(r) is the maximum value we can get with a remaining capacity r
# each value of r gives us a subproblem
# if we don't use the last unit of the capacity, m(r) = m(r-1)
# if we choose object i, m(r) = v[i] + m(r-w[i])

# a memoized recursive solution to the unbounded integer knapsack problem
