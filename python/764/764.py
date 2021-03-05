#leetcode 764 Min Cost climbing stairs
# essentially the same as the normal climbing stairs question: build dp bottom up and add the minimum cost at each step
def minCostClimbingStairs(cost: List[int]) -> int:
    for i in range(2, len(cost)):
        cost[i]+=min(cost[i-1], cost[i-2])
    return min(cost[len(cost)-1], cost[len(cost)-2] )