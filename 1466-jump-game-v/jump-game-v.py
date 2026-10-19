
class Solution(object):
    def maxJumps(self, arr, d):
        n = len(arr)
        dp = [0] * n

        def jump(i):
            if dp[i] != 0:
                return dp[i]

            dp[i] = 1

            for direction in [-1, 1]:
                for step in range(1, d + 1):
                    j = i + direction * step

                    if j < 0 or j >= n:
                        break

                    if arr[j] >= arr[i]:
                        break

                    dp[i] = max(dp[i], 1 + jump(j))

            return dp[i]

        answer = 0

        for i in range(n):
            answer = max(answer, jump(i))

        return answer


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna