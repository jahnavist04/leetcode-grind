
class Solution(object):
    def numberOfSpecialChars(self, word):
        count = 0

        for ch in set(word):
            if ch.islower() and ch.upper() in word:
                count += 1

        return count


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna