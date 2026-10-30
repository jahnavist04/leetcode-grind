
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        original = x
        rev = 0

        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10

        return original == rev


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna