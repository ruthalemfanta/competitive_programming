class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total_cost = 0
        def b(cost):
            return cost[1] - cost[0]

        costs.sort(key=b, reverse=True)
        for i in range(len(costs)//2):
            total_cost += costs[i][0]

        for j in range(len(costs)//2, len(costs)):
            total_cost += costs[j][1]

        return total_cost 

        