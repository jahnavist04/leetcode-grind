class Solution(object):
    def validPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                skipleft,skipright = s[left + 1:right + 1], s[left:right]
                return (skipleft == skipleft[::-1] 
                 or skipright == skipright[::-1])
            left, right = left + 1, right - 1
        return True


                 
            

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna