
class Solution(object):
    def myAtoi(self, s):
        i = 0
        n = len(s)
        sign = 1
        num = 0

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # Check sign
        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # Read digits
        while i < n and s[i].isdigit():
            digit = int(s[i])
            num = num * 10 + digit
            i += 1

        num *= sign

        # Handle overflow
        if num > INT_MAX:
            return INT_MAX
        if num < INT_MIN:
            return INT_MIN

        return num


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna