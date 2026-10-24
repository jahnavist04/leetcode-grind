class Solution(object):
    def minElement(self, nums):
        digit_sums = []

        for num in nums:
            total = 0

            while num > 0:
                total += num % 10
                num //= 10

            digit_sums.append(total)

        return min(digit_sums)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna