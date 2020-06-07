# There are 2N people a company is planning to interview.
# The cost of flying the i-th person to city A is costs[i][0],
# and the cost of flying the i-th person to city B is costs[i][1].

# Return the minimum cost to fly every person to a city such
# that exactly N people arrive in each city.


class Solution:
    def twoCitySchedCost(self, costs):
        cityA = [i for i, j in costs]
        diff = [j - i for i, j in costs]
        return sum(cityA) + sum(sorted(diff)[:len(costs)//2])


print(Solution().twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]))
# output : 110
