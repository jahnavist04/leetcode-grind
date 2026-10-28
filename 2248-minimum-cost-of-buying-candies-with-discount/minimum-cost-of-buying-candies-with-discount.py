class Solution(object):
    def minimumCost(self, cost):
        cost.sort(reverse=True)
        total = 0

        for i in range(len(cost)):
            if (i + 1) % 3 != 0:
                total += cost[i]

        return total

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna