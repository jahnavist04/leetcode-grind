
class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        ans = float('inf')

        for i in range(len(landStartTime)):
            landEnd = landStartTime[i] + landDuration[i]

            for j in range(len(waterStartTime)):
                waterEnd = max(landEnd, waterStartTime[j]) + waterDuration[j]
                ans = min(ans, waterEnd)

        for j in range(len(waterStartTime)):
            waterEnd = waterStartTime[j] + waterDuration[j]

            for i in range(len(landStartTime)):
                landEnd = max(waterEnd, landStartTime[i]) + landDuration[i]
                ans = min(ans, landEnd)

        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna